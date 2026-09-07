import json
from pathlib import Path


def write_json(rows: list[dict], path: str | Path) -> None:
    serializable = [{key: value.isoformat() if hasattr(value, "isoformat") else value for key, value in row.items()} for row in rows]
    Path(path).write_text(json.dumps(serializable, indent=2), encoding="utf-8")
