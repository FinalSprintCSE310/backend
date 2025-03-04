from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

Server = FastAPI()

Origin = "http://localhost:5173"
Server.add_middleware(CORSMiddleware, allow_origins=[Origin], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# Routes for the application will be added here

@Server.get("/")
async def Root():
    return "Entry Point"