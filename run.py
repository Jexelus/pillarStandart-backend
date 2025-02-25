#fastapi
from fastapi import FastAPI
from api.routers import v1
from starlette.middleware.cors import CORSMiddleware

#dotenv
from dotenv import load_dotenv
import os
load_dotenv()

app = FastAPI()

app.include_router(v1.router)


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8090",
    "http://localhost:3000",
    "http://127.0.0.1",
    "http://127.0.0.1:8080",
    "http://127.0.0.1:8090",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT")))
