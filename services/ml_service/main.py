from fastapi import FastAPI
from pydantic import BaseModel

try:
    from .api_handler import FastAPIHandler
except ImportError:
    from api_handler import FastAPIHandler


app = FastAPI()

handler = FastAPIHandler()


class Car(BaseModel):
    Age: int
    Present_Price: float
    Driven_kms: int
    Fuel_Type: str
    Selling_type: str
    Transmission: str


@app.get("/")
def root():
    return {"Hello": "World"}


@app.post("/api/prediction")
def prediction(item_id: int, car: Car):
    price = handler.predict(car.model_dump())

    return {
        "item_id": item_id,
        "price": price
    }