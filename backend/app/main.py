from fastapi import FastAPI

app = FastAPI(
    title="JobOS API",
    description="Personal AI-powered job search and application system",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "app": "JobOS",
        "status": "running",
        "version": "0.1.0",
    }