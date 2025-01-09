FROM python:3.9

WORKDIR /app

COPY receiver.py requirements.txt 

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","receiver.py"] 