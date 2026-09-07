import csv
from pathlib import Path


def read_csv(path: str | Path) -> list[dict[str, str]]:
    with Path(path).open(newline="", encoding="utf-8") as source:
        return list(csv.DictReader(source))
