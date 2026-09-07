PYTHON ?= python

.PHONY: install test run format

install:
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYTHON) -m pytest -q

run:
	$(PYTHON) -m uvicorn business_sentinel.api.routes:app --reload

format:
	$(PYTHON) -m compileall -q src config
