from fastapi import APIRouter, Body, Response, status, HTTPException, Request
from controller.user import AddNewUserAccount_Controller, CheckIfUserExist_Controller, UserLogin_Controller, SetUserLoginCookie_Controller
from models.user import CreateUser_Model, UserLogin_Model


Router = APIRouter()

"""
{
    "Firstname": "str",
    "Lastname": "str",
    "Gender": "str",
    "DateOfBirth": "date",
    "Email": "str",
    "Password": "str",
    "Role": "str",
    "SchoolId": int
}
{
    "Email":"str",
    "Password":"str"
}
"""

@Router.post("/register")
async def CreateNewUser_Route(User: CreateUser_Model = Body(...)):
    Firstname = User.Firstname
    Lastname = User.Lastname
    Gender = User.Gender
    DateOfBirth = User.DateOfBirth
    Email = User.Email
    Password = User.Password
    Role = User.Role
    SchoolId = User.SchoolId
    EmailCheck = CheckIfUserExist_Controller(Email, "Email")
    if EmailCheck is not None:
        return {'USER_EXIST'}
    else:
        try:
            AddNewUserAccount_Controller(Firstname, Lastname, Gender, DateOfBirth, Email, Password, Role, SchoolId)
            return Response(status_code=status.HTTP_201_CREATED)
        except:
            return Response(status_code=status.HTTP_400_BAD_REQUEST)

@Router.post("/login")
async def LoginExistingUser_Route(response: Response, User: UserLogin_Model = Body(...)):
    Email = User.Email
    Password = User.Password
    CheckAuth = UserLogin_Controller(Email, Password)
    if CheckAuth is not None:
        SetUserLoginCookie_Controller(CheckAuth[0], CheckAuth[1], response)
        return True
    else:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)

@Router.get("/login")
async def GetCookieIfExist_Route(request: Request):
    Cookie = request.cookies.get("User_Session_Cookie", None)
    if Cookie:
        print(Cookie)
        return True
    return {"USER_SESSION_EXPIRED"}

"""
User Login:-
email: ashish@email.com
password: ashish@123

email: sarah@email.com
password: sarah@123

email: albert@email.com
password: albert@123
"""