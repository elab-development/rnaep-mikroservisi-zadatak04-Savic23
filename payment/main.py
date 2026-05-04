from fastapi import FastAPI
import requests
import redis
from config import settings

app = FastAPI()

r = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
    decode_responses=True
)

@app.post("/order/{product_id}")
def create_order(product_id: str):

    res = requests.get(f"{settings.INVENTORY_URL}/check/{product_id}")
    available = res.json()["available"]

    if not available:
        return {"status": "failed"}

    order_id = product_id + "_123"

    r.xadd("order_completed", {"order_id": order_id})

    return {"status": "success", "order_id": order_id}