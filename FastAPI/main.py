from typing import Union
from fastapi import FastAPI

app = FastAPI()

# Server start: uvicorn main:app --reload
# Server stop: CTRL+C
# Documentation using Swagger http://127.0.0.1:8000/docs
# Documentation using Redocly http://127.0.0.1:8000/redoc

@app.get("/")
async def read_root():
    return {"Hello": "world!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

