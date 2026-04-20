from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="AI Bug Assistant")

# Allow frontend (React) to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class BugRequest(BaseModel):
    problem: str


@app.get("/")
def home():
    return {"message": "AI Bug Assistant is running 🚀"}


@app.post("/solve")
def solve_bug(request: BugRequest):
    problem = request.problem.lower()

    # ---------------------------
    # SIMPLE RULE-BASED AI ENGINE
    # ---------------------------

    if "null" in problem or "none" in problem:
        return {
            "result": (
                "Cause: Null/None reference error\n"
                "Fix: Add null checks before accessing variables\n"
                "Example:\n"
                "if obj is not None:\n    print(obj)"
            )
        }

    if "react" in problem or "state" in problem:
        return {
            "result": (
                "Cause: React state not updating correctly (async batching or mutation)\n"
                "Fix: Always use setState and avoid direct mutation\n"
                "Example:\n"
                "setData(prev => [...prev, newItem])"
            )
        }

    if "api" in problem or "fetch" in problem:
        return {
            "result": (
                "Cause: API request failure or incorrect endpoint\n"
                "Fix: Check URL, method, headers, and async handling\n"
                "Example:\n"
                "const res = await fetch(url)\nconst data = await res.json()"
            )
        }

    if "cors" in problem:
        return {
            "result": (
                "Cause: CORS policy blocking frontend request\n"
                "Fix: Enable CORS middleware in backend\n"
                "Example:\n"
                "allow_origins=['*'] in FastAPI CORSMiddleware"
            )
        }

    if "sql" in problem or "database" in problem:
        return {
            "result": (
                "Cause: Database query or connection issue\n"
                "Fix: Check SQL syntax and connection string\n"
                "Example:\n"
                "SELECT * FROM users;"
            )
        }

    # Default fallback
    return {
        "result": (
            "Cause: Generic software bug or runtime issue\n"
            "Fix: Debug step-by-step using logs and breakpoints\n"
            "Example:\n"
            "print(variable) or use debugger"
        )
    }