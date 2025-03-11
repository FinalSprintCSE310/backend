from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routes Imports
from routes.register import Router as Register


Server = FastAPI()

Server.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])

# Initiating the Routers that are being pulled from the Routes
Server.include_router(Register, prefix='/api/register')


@Server.get("/")
async def Root():
    return True

# This is for the original Dev Server
    # fastapi dev main.py  
    # uvicorn main:Server --reload  
    
# This is for the Production server
    # fastapi run main.py



# Connect to the database