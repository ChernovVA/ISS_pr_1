from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_client import Histogram, Counter, make_asgi_app

try:
    from .api_handler import FastAPIHandler
except ImportError:
    from api_handler import FastAPIHandler


app = FastAPI()

prediction_histogram = Histogram(
    "car_prediction_price",
    "Distribution of predicted car prices",
    buckets=(0.5, 1, 2, 3, 5, 7, 10, 15, 20, 30, 50)
)

http_requests = Counter(
    "car_http_requests",
    "Number of HTTP requests",
    ["method", "path", "status"]
)

app.mount("/metrics", make_asgi_app())


@app.middleware("http")
async def count_requests(request, call_next):
    try:
        response = await call_next(request)
        status_code = response.status_code
    except Exception:
        status_code = 500
        raise
    finally:
        route = request.scope.get("route")
        path = route.path if route else request.url.path
        http_requests.labels(
            method=request.method,
            path=path,
            status=str(status_code)
        ).inc()
    return response


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
    prediction_histogram.observe(price)

    return {
        "item_id": item_id,
        "price": price,
    }