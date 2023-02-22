from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
async def getUsers():
    return {"users":"user1"}