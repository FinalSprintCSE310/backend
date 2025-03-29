from fastapi import APIRouter, Response, status
from controller.open import GetAllSchools_Controller

Router = APIRouter()

@Router.get("/schools")
async def GetAllSchools_Route():
    Result = GetAllSchools_Controller()
    if not Result:
        return False
    return Result