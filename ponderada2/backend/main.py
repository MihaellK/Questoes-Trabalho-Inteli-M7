import uvicorn
from fastapi import FastAPI, Body, Depends

from app.model import NoteSchema, UserSchema, UserLoginSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer

notes = [
    {
        "id" : 1,
        "content" : "Terminar ponderada de Prog",
        "done" : False
    },
    {
        "id" : 2,
        "content" : "Dockerizar",
        "done" : False
    },
    {
        "id" : 3,
        "content" : "Comprar presente",
        "done" : False
    },
]

users = []

app = FastAPI()

# Get note
@app.get("/notes", tags=["Notes"])
def get_notes():
    return{"data" : notes}

# Get single note by id
@app.get("/notes/{id}", tags=["Notes"])
def get_one_note(id : int):
    if id > len(notes):
        return {
            "error" : "This note id does not exist!"
        }
    for note in notes:
        if note["id"] == id:
            return {
                "data" : note
            }

# Post a new note (handler for creating a note)
@app.post('/notes', dependencies=[Depends(jwtBearer())], tags=["posts"])
def add_note(note : NoteSchema):
    note.id = len(notes) + 1
    notes.append(note.dict())
    return {
        "info" : "note added" 
    }

#  User Signup (Create new User)
@app.post("/user/signup", tags=["user"])
def user_signup(user : UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)

# check if the user already exist 
def check_user(data : UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False
    
@app.post("/user/login", tags=["user"])
def user_login(user : UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "Error" : "invalid login details"
        } 
