from pydantic import BaseModel

class CreateSchool(BaseModel):
    Name: str
    Abb: str
    Zip: int
    Email: str
    MasterUser: str
    MasterPass: str

class CreateUser(BaseModel):
    Firstname: str
    Lastname: str
    Email: str
    Password: str
    IsTeacher: bool
    IsStudent: bool
    IsParent: bool