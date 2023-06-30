venv_name := .venv
sources := src tests

help:
	@echo "lint - check style with ruff and mypy"
	@echo "format - format style with black and isort"
	@echo "tests - run tests quickly with pytest"
	@echo "venv - creates virtual environment"
	@echo "install - install requirements"
	@echo "install-dev - install dev requirements"
	@echo "install-test - install test requirements"	
	@echo "clean - remove venv"	
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-git - remove ignored and not ignored files"

lint:
	python -m ruff $(sources)
	python -m mypy $(sources)

format:
	python -m black $(sources)
	python -m isort $(sources)

test:
	python -m pytest -vv

venv:
	python3 -m virtualenv $(venv_name)

install: 
	pip install .

install-dev: 
	pip install .[dev]

install-test: 
	pip install .[test]

clean: 
	rm -rf $(venv_name)

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean-git:
	git clean -fxd
