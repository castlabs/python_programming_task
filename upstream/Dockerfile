FROM python:3.11.4-slim-bullseye

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY start.py /app/
COPY src /app/src

EXPOSE 8080

CMD ["/app/start.py"]
