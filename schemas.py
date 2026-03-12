from fastapi import APIRouter
from database import users_collection
from schemas import User

router = APIRouter()

@router.get("/users")
def list_users():
    users = []

    for user in users_collection.find():
        user["_id"] = str(user["_id"])
        users.append(user)
    return user

@router.post("/create_users")
def create_users(user: User):
    users_collection.insert_one(user)
    return {"Message": "Usuário criado"}