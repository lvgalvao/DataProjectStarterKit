install:
	poetry install
format:
	isort .
	black .
test:
	pytest -v
run:
	python3 app/main.py
