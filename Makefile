install:
	poetry install
format:
	isort .
	black .
kill:
	kill -9 $(shell lsof -t -i :8000)
test:
	pytest -v
run:
	python3 app/main.py
doc:
	mkdocs serve