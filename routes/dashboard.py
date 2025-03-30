from fastapi import APIRouter, Body, Response, status, HTTPException, Request
from controller.dashboard import GetUsersForAuth_Controller, AuthorizeUser_Controller, GetAllParents_Controller
from helper.helper import GetSchoolIdFromCookie

Router = APIRouter()

@Router.get("/school/auth")
async def GetAllUnAuthUsers_Route(request: Request):
    try:
        SchoolId = GetSchoolIdFromCookie(request)
        Users = GetUsersForAuth_Controller(SchoolId)
        return Users
    except:
        return Response(status_code=status.HTTP_401_UNAUTHORIZED)

@Router.post("/school/auth/parent/{UserId}")
async def AuthorizeUser_Route(UserId: int):
    try:
        AuthorizeUser_Controller(UserId, "Parent")
        return Response(status_code=status.HTTP_201_CREATED)
    except:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

@Router.post("/school/auth/teacher/{UserId}")
async def AuthorizeUser_Route(UserId: int):
    try:
        AuthorizeUser_Controller(UserId, "Teacher")
        return Response(status_code=status.HTTP_201_CREATED)
    except:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

@Router.post("/school/auth/student/{UserId}")
async def AuthorizeUser_Route(UserId: int):
    try:
        AuthorizeUser_Controller(UserId, "Student")
        return Response(status_code=status.HTTP_201_CREATED)
    except:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

@Router.get("/school/parents")
async def GetAllParents_Route(request: Request):
    try:
        SchoolId = GetSchoolIdFromCookie(request)
        Parents = GetAllParents_Controller(SchoolId)
        return Parents
    except:
        return Response(status_code=status.HTTP_401_UNAUTHORIZED)