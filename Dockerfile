FROM python:3.10-slim

WORKDIR /app

COPY src/ .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "github-access-google.py"]
