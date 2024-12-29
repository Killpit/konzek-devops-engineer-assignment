FROM python:3.10-slim

WORKDIR /app

COPY main.py . 

RUN python3 -m venv /app/venv

RUN . /app/venv/bin/activate

EXPOSE 3000

CMD ["/app/venv/bin/python", "main.py"]