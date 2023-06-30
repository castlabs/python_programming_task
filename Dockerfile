FROM python:3.11.4-slim-bullseye

WORKDIR /app

# install project
COPY pyproject.toml setup.py start.py .
COPY src ./src
RUN pip install -e .

EXPOSE 8080
CMD ["./start.py"]
