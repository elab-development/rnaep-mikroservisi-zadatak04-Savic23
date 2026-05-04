from fastapi import FastAPI

app = FastAPI()

inventory = {"1": 10, "2": 5}

@app.get("/check/{product_id}")
def check(product_id: str):
    return {"available": inventory.get(product_id, 0) > 0}