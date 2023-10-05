PYTHON_VERSION=3.11.3
PYTHON_PATH=$(shell pyenv which python)

setup:
	@if ! pyenv versions | grep -q $(PYTHON_VERSION); then \
		pyenv install $(PYTHON_VERSION); \
	fi
	pyenv local $(PYTHON_VERSION)
	poetry env use $(PYTHON_VERSION)
	poetry install
	poetry shell

format:
	isort .
	black .
kill:
	kill -9 $(shell lsof -t -i :8000)
test:
	pytest -v

run: setup
	python3 app/main.py
doc:
	mkdocs serve