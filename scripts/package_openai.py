#!/usr/bin/env python3
"""Validate and package Yazıhane's portable, skills-only OpenAI plugin."""

import argparse
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET
import zipfile


ROOT = Path(__file__).resolve().parents[1]
ROOT_FILES = ("plugin.json", "LICENSE")
RUNTIME_DIRS = ("skills", "templates", "assets")


def package_files(root):
    paths = [root / name for name in ROOT_FILES]
    for name in RUNTIME_DIRS:
        folder = root / name
        if not folder.is_dir():
            raise ValueError(f"Missing runtime directory: {name}")
        for path in sorted(folder.rglob("*")):
            if path.is_symlink():
                raise ValueError(f"Symlink is not a packaged resource: {path.relative_to(root)}")
            if path.is_file() and not any(
                part.startswith(".") or part == "__pycache__"
                for part in path.relative_to(folder).parts
            ):
                paths.append(path)
    for path in paths:
        if not path.is_file() or path.is_symlink():
            raise ValueError(f"Missing or unsafe package file: {path.relative_to(root)}")
    return sorted(paths)


def packaged_path(root, value, included):
    path = (root / value).resolve()
    if not path.is_relative_to(root.resolve()) or path not in included:
        raise ValueError(f"Resource is outside the package or missing: {value}")
    return path


def validate(root, paths):
    manifest = json.loads((root / "plugin.json").read_text(encoding="utf-8"))
    if manifest.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        raise ValueError("Expected a portable Agent Plugins manifest")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", manifest["name"]):
        raise ValueError("Invalid plugin identifier")
    if not re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"]):
        raise ValueError("Use a three-part release version")
    claude = json.loads((root / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
    if (manifest["name"], manifest["version"]) != (claude["name"], claude["version"]):
        raise ValueError("Portable and Claude manifests must identify the same version")
    extension = manifest["extensions"]["com.openai"]
    if any(key in extension for key in ("apps", "hooks", "mcpServers")):
        raise ValueError("This public package is skills-only")
    interface = extension["interface"]
    for field, maximum in {
        "displayName": 30, "shortDescription": 30,
        "longDescription": 4000, "developerName": 80,
    }.items():
        value = interface.get(field)
        if not isinstance(value, str) or not value.strip() or len(value) > maximum:
            raise ValueError(f"Invalid listing field: {field} (limit {maximum})")
    if not interface.get("category"):
        raise ValueError("A listing category is required")
    prompts = interface.get("defaultPrompt", [])
    if not isinstance(prompts, list) or len(prompts) > 3 or any(
        not isinstance(prompt, str) or not prompt.strip() or len(prompt) > 128
        for prompt in prompts
    ):
        raise ValueError("Provide at most three starter prompts of 128 characters")
    included = {path.resolve() for path in paths}
    for field in ("logo", "composerIcon"):
        path = packaged_path(root, interface[field], included)
        if path.stat().st_size > 5 * 1024 * 1024:
            raise ValueError(f"Icon exceeds 5 MiB: {path.name}")
        if path.suffix == ".svg":
            svg = ET.parse(path).getroot()
            width, height = float(svg.attrib["width"]), float(svg.attrib["height"])
            if width != height or width < 48:
                raise ValueError(f"Icon must be square and at least 48px: {path.name}")
    for translation in extension.get("publication", {}).get("translations", {}).values():
        for field, maximum in (("subtitle", 30), ("description", 4000)):
            value = translation.get(field)
            if value is not None and (not value.strip() or len(value) > maximum):
                raise ValueError(f"Translation exceeds the {field} limit")

    skills = sorted((root / "skills").glob("*/SKILL.md"))
    if not skills:
        raise ValueError("At least one skill is required")
    for path in skills:
        text = path.read_text(encoding="utf-8")
        header = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        if not header:
            raise ValueError(f"Missing skill frontmatter: {path.relative_to(root)}")
        fields = dict(line.split(":", 1) for line in header[1].splitlines())
        if set(fields) != {"name", "description"}:
            raise ValueError(f"Expected portable skill metadata: {path.relative_to(root)}")
        if fields["name"].strip() != path.parent.name or not fields["description"].strip():
            raise ValueError(f"Invalid skill name/description: {path.relative_to(root)}")
    for path in paths:
        if path.suffix != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        if any(token in text for token in ("CLAUDE_PLUGIN_ROOT", "$ARGUMENTS")):
            raise ValueError(f"Provider-specific expansion in runtime file: {path.relative_to(root)}")
        # Check bundled Markdown links and literal relative resource paths.
        candidates = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
        candidates += re.findall(r"`((?:\.\.?/|references/|rehber/|sablonlar/)[^`]+)`", text)
        for value in candidates:
            if "://" in value or value.startswith("#") or any(c in value for c in "<>*|"):
                continue
            value = value.split("#", 1)[0]
            target = (path.parent / value).resolve()
            if target.is_dir():
                if not any(p.is_relative_to(target) for p in included):
                    raise ValueError(f"Unpackaged directory: {value}")
            elif target not in included:
                raise ValueError(f"Broken reference in {path.relative_to(root)}: {value}")
    roles = {p.stem for p in (root / "agents").glob("*.md")}
    for role in roles:
        packaged_path(root, f"skills/editor/references/okurlar/{role}.md", included)
    return manifest, len(skills)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate without writing a ZIP")
    parser.add_argument("--output", type=Path, help="destination ZIP path")
    args = parser.parse_args()
    try:
        paths = package_files(ROOT)
        manifest, count = validate(ROOT, paths)
        if args.check:
            print(f"Valid: {manifest['name']} {manifest['version']}; {count} skills; {len(paths)} runtime files")
            return 0
        output = args.output or ROOT / "dist" / f"yazihane-openai-{manifest['version']}.zip"
        if (
            output.resolve() in {path.resolve() for path in paths}
            or output.suffix != ".zip"
            or any(output.resolve().is_relative_to(ROOT / name) for name in RUNTIME_DIRS)
        ):
            raise ValueError("Output must be a separate .zip file")
        output.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for path in paths:
                info = zipfile.ZipInfo(path.relative_to(ROOT).as_posix(), date_time=(2020, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, path.read_bytes())
        print(f"Created {output} ({count} skills, {len(paths)} runtime files)")
        return 0
    except (ValueError, KeyError, OSError, ET.ParseError) as error:
        print(f"Package error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
