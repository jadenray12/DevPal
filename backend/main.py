from fastapi import FastAPI

app = FastAPI(title="DevPal Local Server")

@app.get("/")
def root():
    return {"message": "DevPal server running!"}

@app.post("/commit")
def generate_commit(message: str):
    # Placeholder for commit generation logic
    return {"commit_message": f"Generated commit: {message}"}

@app.post("/summarize")
def summarize_code():
    # Placeholder for summarize logic
    return {"summary": "This will summarize code changes."}
