# API for using basic authentication (user/pass)

from fastapi import FastAPI, Depends, HTTPException, status, Header
from pydantic import BaseModel
# Import for using OAuth2 basic authentication 
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

# instance for OAuth2 using based token URL
oauth2 = OAuth2PasswordBearer(tokenUrl="/login")

# basic user class
class User(BaseModel):
    username: str
    fullName: str
    email: str
    disabled: bool

# user class for DB
class UserDB(User):
    password: str

# Temporal list of users simulating DB content 
usersDB = {
    "alan.altamirano": {
        "username": "alan.altamirano",
        "fullName": "Alan Altamirano",
        "email": "alan.altamirano@somedomainz.com",
        "disabled": False,
        "password": "123456"
    },
    "fernando.altamirano": {
        "username": "fernando.altamirano",
        "fullName": "Fernando Altamirano",
        "email": "fernando.altamirano@somedomainz.com",
        "disabled": True,
        "password": "987654"
    }     
}

# function that search and return a new User based on a given username 
def search_user(username: str):
    if username in usersDB:
        return User(**usersDB[username])
    
# async function to get current authenticated user which depends on OAuth2
async def get_current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, 
                            detail="Invalid auth credentials!",
                            headers={"WWW-Authenticate": "Bearer"})
    if user.disabled:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, 
                            detail="Inactive user")    
    return user

# post operation to get login OAuth2 token
@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    dbUser = usersDB.get(form.username)
    print("dbUser: ", dbUser)
    # validate that ser exists
    if not dbUser:
        raise HTTPException(status_code=400, detail="Incorrect user")
    
    # validate user match with pass
    if not dbUser['password'] == form.password:
        raise HTTPException(status_code=400, detail="Incorrect password")
    
    return {"access_token": form.username, "token_type": "bearer"}

# this API operation return the current user which depends on OAuth2 authentication
@app.get("/users/me")
async def get_me(user: User = Depends(get_current_user)):
    return user
