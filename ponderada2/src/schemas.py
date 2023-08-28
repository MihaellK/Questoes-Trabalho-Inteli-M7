from pydantic import BaseModel


class NoteBase(BaseModel):
    description: str | None = None


class NoteCreate(NoteBase):
    pass


class Note(NoteBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    notes: list[Note] = []

    class Config:
        orm_mode = True
