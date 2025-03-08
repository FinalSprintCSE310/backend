from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Testing
from db.execute import ConnectionString, QueryResult

Server = FastAPI()

Server.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])


@Server.get("/")
async def Root():
    return True

# fastapi dev server.py
# uvicorn main:Server --reload  



# Connect to the database