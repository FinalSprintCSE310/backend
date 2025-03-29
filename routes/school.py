from fastapi import APIRouter, Body, Response, status, HTTPException, Request
from controller.school import CheckIfUserExist_Controller, AddNewSchoolAccount_Controller, SchoolLogin_Controller, SetSchoolLoginCookie_Controller
from models.user import CreateSchool_Model, SchoolLogin_Model
Router = APIRouter()

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
{
    "Email": string,
    "Password": string
}
"""
@Router.post("/login")
async def LoginExistingSchool_Route(response: Response, School: SchoolLogin_Model = Body(...)):
    Email = School.Email
    Password = School.Password
    CheckAuth = SchoolLogin_Controller(Email, Password)
    if CheckAuth is not None:
        SetSchoolLoginCookie_Controller(CheckAuth[0], response)
        return True
    else:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)

@Router.get("/login")
async def GetCookieIfExist_Route(request: Request):
    Cookie = request.cookies.get("School_Session_Cookie", None)
    if Cookie:
        print(Cookie)
        return True
    return {"ORG_SESSION_EXPIRED"}

# Create a dashboard and should have details about, Students & Parents (Just Show all their Info), Faculty(Info and all the classes they teach), Auth(Students, Parents, Teachers)