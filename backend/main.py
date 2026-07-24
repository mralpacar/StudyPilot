from fastapi import FastAPI

app = FastAPI(
    title="StudyPilot API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to StudyPilot!"
    }