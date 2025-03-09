from fastapi import APIRouter, Body, Response, status, HTTPException
from controller.school import GetAllSchoolsController

Router = APIRouter()

@Router.get("/school")
async def GetAllSchools():
    Result = GetAllSchoolsController()
    if not Result:
        return False
    return Result