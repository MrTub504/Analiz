import json
import sys
from pathlib import Path

src = Path(sys.argv[1])
dst = Path(sys.argv[2])
raw = src.read_text(encoding="utf-8")
obj = json.loads(raw)


def dedupe_case_conflicts(value):
    if isinstance(value, dict):
        out = {}
        seen = set()
        for key, item in value.items():
            key_norm = str(key).casefold()
            if key_norm in seen:
                continue
            seen.add(key_norm)
            out[key] = dedupe_case_conflicts(item)
        return out
    if isinstance(value, list):
        return [dedupe_case_conflicts(item) for item in value]
    return value


normalized = dedupe_case_conflicts(obj)
dst.write_text(json.dumps(normalized, ensure_ascii=False, indent=2), encoding="utf-8")