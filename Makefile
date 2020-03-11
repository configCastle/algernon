export PYTHONPATH=.

all: run

run:
	@python app.py

test:
	@py.test algernon

lint:
	@flake8

write_service:
	@python scripts/write_service.py
