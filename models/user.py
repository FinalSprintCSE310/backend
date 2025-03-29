from pydantic import BaseModel
from datetime import date

class CreateSchool_Model(BaseModel):
    Name: str
    Abbr: str
    Zip: int
    Email: str
    Password: str

class SchoolLogin_Model(BaseModel):
    Email: str
    Password: str

class CreateUser_Model(BaseModel):
    Firstname: str
    Lastname: str
    Gender: str
    DateOfBirth: date
    Email: str
    Password: str
    Role: str
    SchoolId: int
class UserLogin_Model(BaseModel):
    Email: str
    Password: str
class TestModel(BaseModel):
    Email: str
    Route: str