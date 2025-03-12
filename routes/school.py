from fastapi import APIRouter, Body, Response, status, HTTPException
from controller.school import GetAllSchools_Controller, CheckIfUserExist_Controller
from models.user import CreateSchool_Model, TestModel
Router = APIRouter()

@Router.get("/")
async def GetAllSchools_Route():
    Result = GetAllSchools_Controller()
    if not Result:
        return False
    return Result

@Router.post("/register")
# async def CreateNewSchool_Route(School: CreateSchool_Model = Body(...)):
async def CreateNewSchool_Route(School: TestModel = Body(...)):
    Email = CheckIfUserExist_Controller(School.Email, "Email")
    Route = CheckIfUserExist_Controller(School.Route, "Route")
    if Route is not None:
        return {'USER_EXIST'}
    elif Email is not None:
        return {'EMAIL_EXIST'}
    else:
        return False
    
"""
{
    "Name": string,
    "Abbr": string,
    "Zip": integer,
    "Email" : string,
    "Password" : string
}
"""
