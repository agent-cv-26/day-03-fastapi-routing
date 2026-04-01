from fastapi import FastAPI

app = FastAPI(title="AI Model Gateway - Day 03")


@app.get("/")
async def root():
    return {"status": "Online", "message": "FastAPI Server is Running"}


# --- أضف هذا الجزء الجديد هنا ---
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # لاحظ أننا حددنا نوع البيانات هنا بـ (int) لنجبر السيرفر على التحقق
    return {"item_id": item_id, "message": "Success! You provided a valid integer."}


# ------------------------------


@app.get("/models/{model_id}")
async def get_model_status(model_id: str):
    return {"model_id": model_id, "framework": "PyTorch/YOLOv8", "is_active": True}
