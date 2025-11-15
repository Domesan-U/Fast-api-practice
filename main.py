from fastapi import FastAPI
import uvicorn
from controller import EventController

app = FastAPI()

app.include_router(EventController.router)

if __name__ =="__main__":
    uvicorn.run("main:app",host="localhost",port=8080)