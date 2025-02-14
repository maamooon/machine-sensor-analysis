from config.db import connectDB
from fastapi import FastAPI
import uvicorn
import os
from routes import router

app = FastAPI()

app.include_router(router)


PORT = int(os.getenv("PORT"))
HOST = os.getenv("HOST")

if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
    print(f"Server is running on {HOST}:{PORT}")