from business_sentinel.database.connection import get_connection
from business_sentinel.risk.case_manager import create_case, list_cases


def test_case_persistence(tmp_path, monkeypatch):
    monkeypatch.setenv('BUSINESS_SENTINEL_DATABASE_URL', f'sqlite:///{tmp_path / "test.db"}')
    connection = get_connection()
    create_case(connection, {"title": "Review", "description": "Test", "score": 70, "entity_type": "invoice", "entity_id": "1"})
    assert len(list_cases(connection)) == 1
