import os
import random
import time

import httpx


# Адрес сервиса предсказаний
API_URL = os.getenv(
    "API_URL",
    "http://localhost:8000/api/prediction"
)

item_id = 1

while True:
    car = {
        "Age": random.randint(0, 10),
        "Present_Price": round(random.uniform(3.0, 15.0), 2),
        "Driven_kms": random.randint(5000, 200000),
        "Fuel_Type": random.choice(["Petrol", "Diesel"]),
        "Selling_type": random.choice(["Dealer", "Individual"]),
        "Transmission": random.choice(["Manual", "Automatic"])
    }

    try:
        response = httpx.post(
            API_URL,
            params={"item_id": item_id},
            json=car,
            timeout=10.0
        )

        print(
            f"ID: {item_id}, "
            f"Status: {response.status_code}, "
            f"Response: {response.text}",
            flush=True
        )

    except httpx.RequestError as error:
        print(f"Ошибка соединения: {error}", flush=True)

    item_id += 1

    time.sleep(random.uniform(0, 5))