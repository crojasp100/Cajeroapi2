from fastapi import FastAPI 
from db.user_db import database_users
from fastapi import HTTPException
from db.user_db import UserInDB
app= FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}


@app.get("/users/")
async def users():
    return {"message": database_users} 


@app.get("/users/{username}")
async def get_user_name(username: str):
    if username in database_users:
        return {"message": database_users[username]}  
    raise HTTPException(status_code=404, detail= "El usuario no existe")

@app.post("/users/")
async def create_user(user: UserInDB):
    database_users[user.username]=user
    return user 

@app.delete("/users/")
async def create_user(user: UserInDB):
    del database_users[user.username]
    return user 
        
@app.put("/users/")
async def create_user(user: UserInDB):
    database_users[user.username]=user
    return user 