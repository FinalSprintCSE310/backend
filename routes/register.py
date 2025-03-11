from fastapi import APIRouter, Body, Response, status, HTTPException
from controller.school import GetAllSchools_Controller, CheckIfUserExist_Controller
from models.user import CreateSchool_Model
Router = APIRouter()

@Router.get("/school")
async def GetAllSchools_Route():
    Result = GetAllSchools_Controller()
    if not Result:
        return False
    return Result

@Router.post("/school")
async def CreateNewSchool_Route(School: CreateSchool_Model = Body(...)):
    Result = CheckIfUserExist_Controller(School.Email)
    if Result is not None:
        return True
    else:
        return False