FROM python:3.8-alpine3.10

WORKDIR /home/python_server
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]