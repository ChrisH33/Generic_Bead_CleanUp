import json
from pathlib import Path

def collect_paths(obj, prefix=""):
    paths = set()
    if isinstance(obj, dict):
        for k, v in obj.items():
            new_prefix = f"{prefix}.{k}" if prefix else k
            paths.add(new_prefix)
            paths |= collect_paths(v, new_prefix)
    elif isinstance(obj, list):
        if obj:
            paths |= collect_paths(obj[0], f"{prefix}[0]")
    return paths

template = json.loads(Path("method.template.json").read_text())
template_paths = collect_paths(template)

failed = False

for method_file in Path(".").glob("*.json"):
    if method_file.name == "method.template.json" or method_file.name.startswith("_"):
        continue

    method = json.loads(method_file.read_text())
    method_paths = collect_paths(method)

    missing = template_paths - method_paths
    if missing:
        print(f"\n✗ {method_file.name} is missing {len(missing)} key(s):")
        for p in sorted(missing):
            print(f"  - {p}")
    else:
        print(f"✓ {method_file.name}")
