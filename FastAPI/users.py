from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Server start: uvicorn users:app --reload
# Server stop: CTRL+C
# Documentation using Swagger http://127.0.0.1:8000/docs
# Documentation using Redocly http://127.0.0.1:8000/redoc

# User model
class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    url: str

users = [User(id=1, name="Alan", surname="Altamirano", age=36, url="https://google.com"),
         User(id=2, name="Fernando", surname="Altamirano", age=26, url="https://google.com"),
         User(id=3, name="Ulises", surname="Altamirano", age=35, url="https://google.com")
         ]

# get users operation
@app.get("/users")
async def getUsers():
    return users

# get users by ID
@app.get("/users/{id}")
async def getUsersById(id: int):
    usersById = filter(lambda user: user.id == id, users)
    try:
        return list(usersById)[0]
    except:
        return {"error":"user not found"}