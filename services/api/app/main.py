import os

from fastapi import FastAPI

app = FastAPI(title=os.getenv("APP_NAME", "SRE Incident Copilot"))


@app.get("/")
def hello() -> dict[str, str]:
    return {"message": "SRE Incident Copilot API is running"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
