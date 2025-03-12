from pydantic import BaseModel

class CreateSchool_Model(BaseModel):
    Name: str
    Abbr: str
    Zip: int
    Email: str
    Password: str

class CreateUser_Model(BaseModel):
    Firstname: str
    Lastname: str
    Email: str
    Password: str
    IsTeacher: bool
    IsStudent: bool
    IsParent: bool

class TestModel(BaseModel):
    Email: str
    Route: str