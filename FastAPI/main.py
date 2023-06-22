# Import to use FastAPI framework
from fastapi import FastAPI
# Import to add routers
from routers import users, products
# Import for accessing static resurces
from fastapi.staticfiles import StaticFiles

# Server start: uvicorn main:app --reload
# Server stop: CTRL+C
# Documentation using Swagger http://127.0.0.1:8000/docs
# Documentation using Redocly http://127.0.0.1:8000/redoc

app = FastAPI()

# Adding routers to the main API
app.include_router(users.router)
app.include_router(products.router)

# adding mount point for accessing static resources
app.mount("/static", StaticFiles(directory="static"), name="static")

# Home opertion in main API
# adding comment
@app.get("/")
async def read_root():
    return {"message": "Hello world!"}
