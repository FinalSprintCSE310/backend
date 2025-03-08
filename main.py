from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# TEsting 
import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")


Server = FastAPI()

Server.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])


@Server.get("/")
async def Root():
    return{"Routes": [
        {"Create User" : "POST, /api/create/user"},
        {"Create Task" : "POST, /api/create/task"}
        ]}

# fastapi dev server.py
# uvicorn main:Server --reload  



# Connect to the database