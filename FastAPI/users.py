from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Allows main API having access to the resources of users API
router = APIRouter(prefix="/users")

# User model
class User(BaseModel):
    id: int
    name: str
    alias: str
    age: int
    url: str

users = [User(id=1, name="Charles Xavier", alias="Professor-X", age=55, url="https://www.marvel.com/characters/professor-x"),
         User(id=2, name="James Howlett", alias="Wolverine", age=150, url="https://www.marvel.com/characters/wolverine-james-howlett/in-comics"),
         User(id=3, name="Ororo N'Dare", alias="Storm", age=35, url="https://www.marvel.com/characters/storm/in-comics"),
         User(id=4, name="Kurt Wagner", alias="Nightcrawler", age=25, url="https://www.marvel.com/characters/nightcrawler")
         ]

# Get users operation
@router.get("/", response_model=list[User])
async def getUsers():
    return users

# Get users by ID using path variable 
@router.get("/{id}", response_model=User)
async def getUsersById(id: int):
    return searchUser(id)
        
# Get users by ID using query string parameter 
""" @router.get("/users", response_model=User)
async def getUsersById(id: int):
    return searchUser(id) """

# Post operation to add a new user
@router.post("/", response_model=User, status_code=201)
async def addUser(user: User):
    if type(searchUser(user.id)) == User:
        raise HTTPException(status_code=422, detail="user already exists")
    users.append(user)
    return user

# Put operation to update a user
@router.put("/", response_model=User)
async def updateUser(user: User):
    found: bool = False
    for idx, currentUser in enumerate(users):
        if currentUser.id == user.id:
            users[idx] = user
            found = True
    if not found:
        raise HTTPException(status_code=422, detail="user not found")
    return user

# Delete operation to remove a user
@router.delete("/{id}")
async def deleteUser(id: int):
    found: bool = False
    for idx, currentUser in enumerate(users):
        if currentUser.id == id:
            del users[idx]
            found = True
    if not found:
        raise HTTPException(status_code=422, detail="user not found")


# function to return a list of users by ID
def searchUser(id: int):    
    usersById = filter(lambda item: item.id == id, users)
    try:
        return list(usersById)[0]
    except:
        return None
