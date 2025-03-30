from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routes Imports
from routes.school import Router as School
from routes.user import Router as User
from routes.open import Router as Global
from routes.dashboard import Router as Dashboard

Server = FastAPI()

Server.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])

# Initiating the Routers that are being pulled from the Routes
Server.include_router(School, prefix='/api/v1/school')
Server.include_router(User, prefix='/api/v1/user')
Server.include_router(Global, prefix='/api/v1/global')
Server.include_router(Dashboard, prefix='/api/v1/dashboard')


@Server.get("/")
async def Root():
    return True

# This is for the original Dev Server
    # fastapi dev main.py  
    # uvicorn main:Server --reload  
    
# This is for the Production server
    # fastapi run main.py



# Connect to the database