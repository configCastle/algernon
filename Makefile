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

write_test_file:
	@python scripts/write_test_file.py

write:
	@python scripts/write_service.py
	@python scripts/write_test_file.py
