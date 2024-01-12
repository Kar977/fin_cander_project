FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /app/docker-entrypoint.sh

#ADD wait_for_db.py /app

#RUN chmod +x /app/wait_for_db.py

#CMD ["./wait_For_db.py"]