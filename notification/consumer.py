import redis
from config import settings

r = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
    decode_responses=True
)

while True:
    messages = r.xread({
        "order_completed": "0",
        "refund_order": "0"
    }, block=0)

    for stream, msgs in messages:
        for _, data in msgs:
            print(f"NOTIFIKACIJA: order {data.get('order_id')}")