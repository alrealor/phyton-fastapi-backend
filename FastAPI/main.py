from typing import Union
from fastapi import FastAPI
from routers import users, products

# Server start: uvicorn main:app --reload
# Server stop: CTRL+C
# Documentation using Swagger http://127.0.0.1:8000/docs
# Documentation using Redocly http://127.0.0.1:8000/redoc

app = FastAPI()

# Adding routers to the main API
app.include_router(users.router)
app.include_router(products.router)

# Home opertion in main API
@app.get("/")
async def read_root():
    return {"message": "Hello world!"}
