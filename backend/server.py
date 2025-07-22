from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow the browser to call us from any origin (development‑friendly CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class NameIn(BaseModel):
    name: str

@app.get("/api/ping")
async def ping():
    return {"message": "pong"}

@app.post("/api/greet")
async def greet(payload: NameIn):
    return {"message": f"Hello, {payload.name}!"}

@app.post("/api/hate")
async def greet(payload: NameIn):
    return {"message": f"I hate you, {payload.name}!"}
