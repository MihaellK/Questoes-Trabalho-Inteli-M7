from pydantic import BaseModel, Field, EmailStr

class NoteSchema(BaseModel):
    id : int = Field(default=None)
    content : str = Field(default=None)
    done : bool = Field(default=False)

    class Confir:
        schema_extra = {
            "nexample" : {
                "content" : "here a todo note example" 
            }
        }

class UserSchema(BaseModel):
    fullname: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Mihaell Alves",
                "email": "mihaell@email.com",
                "password": "senha123"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        schema_extra = {
            "example": {
                "email": "mihaell@email.com",
                "password": "senha123"
            }
        }