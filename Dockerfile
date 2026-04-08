FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install flask==3.1.2 pyyaml==6.0.3 pydantic==2.12.5

CMD ["python", "inference.py"]