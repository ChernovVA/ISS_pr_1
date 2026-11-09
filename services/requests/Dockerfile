FROM python:3.11-slim

WORKDIR /requests

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-u", "requests.py"]

# Сборка образа из services/requests
# sudo docker build -t car-requests:1 .

# Запуск контейнера в сети Compose
# sudo docker run --rm --network services_default -e API_URL=http://ml_service:8000/api/prediction car-requests:1