
all: build run

build:
	poetry install

run:
	env FLASK_APP=run.py flask run