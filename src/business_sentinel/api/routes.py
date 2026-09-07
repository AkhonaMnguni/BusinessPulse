from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from business_sentinel.database.connection import get_connection
from business_sentinel.risk.case_manager import create_case, list_cases

app = FastAPI(title="Business Sentinel", version="0.1.0")


class AlertRequest(BaseModel):
    title: str = Field(min_length=1)
    description: str = Field(min_length=1)
    score: int = Field(ge=0, le=100)
    entity_type: str = "transaction"
    entity_id: str = "unknown"


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/cases")
def cases() -> list[dict]:
    with get_connection() as connection:
        return list_cases(connection)


@app.post("/api/cases", status_code=201)
def add_case(alert: AlertRequest) -> dict:
    with get_connection() as connection:
        return create_case(connection, alert.model_dump())


@app.get("/api/cases/{case_id}")
def case(case_id: int) -> dict:
    with get_connection() as connection:
        row = connection.execute("SELECT * FROM cases WHERE id = ?", (case_id,)).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Case not found")
    return dict(row)
