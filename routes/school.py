from fastapi import APIRouter, Body, Response, status, HTTPException
from controller.school import GetAllSchools_Controller, CheckIfUserExist_Controller, AddNewSchoolAccount_Controller
from models.user import CreateSchool_Model, TestModel
Router = APIRouter()

@Router.get("/")
async def GetAllSchools_Route():
    Result = GetAllSchools_Controller()
    if not Result:
        return False
    return Result

@Router.post("/register")
async def CreateNewSchool_Route(School: CreateSchool_Model = Body(...)):
    Name = School.Name
    Abbr = School.Abbr
    Zip = School.Zip
    Password = School.Password
    Email = School.Email
    EmailCheck = CheckIfUserExist_Controller(Email, "Email")
    RouteCheck = CheckIfUserExist_Controller(Abbr+'-'+str(Zip), "Route")
    if RouteCheck is not None:
        return {'ORG_EXIST'}
    elif EmailCheck is not None:
        return {'EMAIL_EXIST'}
    else:
        try:
            AddNewSchoolAccount_Controller(Name, Abbr, Zip, Email, Password)
            return Response(status_code=status.HTTP_201_CREATED)
        except:
            return Response(status_code=status.HTTP_400_BAD_REQUEST)
    
"""
{
    "Name": string,
    "Abbr": string,
    "Zip": integer,
    "Email" : string,
    "Password" : string
}
"""
