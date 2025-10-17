import os
from fastapi import FastAPI
from pydantic import BaseModel
import subprocess
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv


load_dotenv()




app = FastAPI(title="DevPal Local Server")



class SummarizeRequest(BaseModel):
    path: str

class CommitRequest(BaseModel):
    message: str


@app.get("/")
def root():
    return {"message": "DevPal server running!!"}

@app.post("/commit")
def generate_commit(message: str):
    # Placeholder for commit generation logic
    return {"commit_message": f"Generated commit PLZ: {message}"}

@app.post("/summarize")
def summarize_code(message: SummarizeRequest):
    try:
        result = subprocess.run(
            ["git", "diff"],
            cwd=message.path,
            capture_output=True,
            text=True,
            check=True
        )

        diff_output = result.stdout.strip()
        if not diff_output:
            return {"summary": "No Changes detected."}   


        llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3)

        prompt = ChatPromptTemplate.from_template("Summarize the following git changes in a clean consise message. This message will be going to a developer that is" \
        "trying to understand what chnages have been made to the repo. Here is the git chnages: \n\n {diff}")

        chain = prompt | llm

        llm_response = chain.invoke({"diff": diff_output})

        summary_text = llm_response.content.strip() 

        return {"summary": summary_text} 

    except subprocess.CalledProcessError as e:
        return {"error": f"Git command failed: {e.stderr.strip()}"}
    except FileNotFoundError:
        return {"error": "Invalid path or git not found."}
    except Exception as e:
        return {"error": f"Unexpected error: {type(e).__name__}: {e}"}