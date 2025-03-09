from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routes
from routes.register import Router as Register


Server = FastAPI()

Server.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])

Server.include_router(Register, prefix='/api/register')

@Server.get("/")
async def Root():
    return True

# fastapi dev server.py
# uvicorn main:Server --reload  



# Connect to the database