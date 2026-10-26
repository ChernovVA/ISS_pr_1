FROM python:3.11-slim

COPY . /ml_service

VOLUME /models

WORKDIR /ml_service

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Сборка Docker-образа (из директории services/ml_service)
# sudo docker build -t car-price-predict-service:1 .

# Запуск контейнера с подключением обученной модели
# sudo docker run --rm --name car-price-api -p 8000:8000 -v "$(pwd)/../models:/models:ro" car-price-predict-service:1