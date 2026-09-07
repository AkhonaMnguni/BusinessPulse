from pathlib import Path

from business_sentinel.etl.extract import read_csv
from business_sentinel.etl.load import write_json
from business_sentinel.etl.transform import normalize_transactions
from business_sentinel.etl.validate import validate_transactions


def run(input_path: str | Path, processed_path: str | Path) -> dict[str, int]:
    rows = normalize_transactions(read_csv(input_path))
    result = validate_transactions(rows)
    write_json(result.valid, processed_path)
    return {"processed": len(result.valid), "quarantined": len(result.invalid)}
