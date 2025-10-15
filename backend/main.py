from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="DevPal Local Server")



class SummarizeRequest(BaseModel):
    path: str


@app.get("/")
def root():
    return {"message": "DevPal server running!"}

@app.post("/commit")
def generate_commit(message: str):
    # Placeholder for commit generation logic
    return {"commit_message": f"Generated commit: {message}"}

@app.post("/summarize")
def summarize_code(message: SummarizeRequest):
    # Placeholder for summarize logic
    return {"summary": f"This will summarize code changes?{message.path}"}
