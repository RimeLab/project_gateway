VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

.PHONY: setup run clean docker-build docker-run docker-down docker-restart

setup:
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

run:
	FLASK_APP=base.py $(PYTHON) -m flask run

clean:
	rm -rf $(VENV) __pycache__

docker-build:
	docker compose build

docker-up:
	docker compose up -d

docker-down:
	docker compose down

docker-restart:
	docker compose restart app
