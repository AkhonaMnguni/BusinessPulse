CREATE VIEW IF NOT EXISTS open_cases AS
SELECT * FROM cases WHERE status = 'open';
