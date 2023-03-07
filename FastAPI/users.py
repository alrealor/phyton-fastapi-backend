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

# Get users by ID using path variable 
@app.get("/users/{id}")
async def getUsersById(id: int):
    return searchUser(id)
        
# Get users by ID using query string parameter 
@app.get("/users/")
async def getUsersById(id: int):
    return searchUser(id)

# Post operation to add a new user
@app.post("/user/")
async def addUser(user: User):
    if type(searchUser(user.id)) == User:
        return {"error": "user already exists"}
    else:
        users.append(user)

# function to return a list of users by ID
def searchUser(id: int):    
    usersById = filter(lambda user: user.id == id, users)
    try:
        return list(usersById)[0]
    except:
        return {"error":"user not found"}