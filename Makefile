
all: build run

build:
	poetry install

run:
	env FLASK_APP=castlabs_proxy/run.py flask run