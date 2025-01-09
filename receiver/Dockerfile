FROM python:3.9

WORKDIR /app1

COPY receiver.py requirements.txt .

# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

CMD ["python","receiver.py"] 