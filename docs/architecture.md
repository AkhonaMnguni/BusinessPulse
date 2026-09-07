# Architecture

Business Sentinel separates ingestion, analytical transformations, explainable risk rules, persistence, and presentation. The initial runtime uses SQLite for local development and exposes a FastAPI service. PostgreSQL can replace the database adapter without changing the analytics contracts.
