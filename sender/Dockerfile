# FROM python:3.9
# WORKDIR /app
# COPY sender.py requirements.txt
# # RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt
# CMD ["python","sender.py"]
FROM python:3.9
WORKDIR /app
COPY  sender.py requirements.txt .
RUN python -m pip install --upgrade pip && python -m pip install -r requirements.txt
CMD ["python","sender.py"]