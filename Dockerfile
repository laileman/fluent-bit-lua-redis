from python:3.12.0b4-slim-bullseye
workdir /app
#run apt-get update && apt-get install -y libpq-dev gcc
copy requirements.txt requirements.txt
run pip install -r requirements.txt
copy . .
entrypoint ["python","main-app.py"]