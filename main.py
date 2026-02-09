from fastapi import FastAPI
from app.routes import router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.include_router(router)


if __name__ == "__main__":
    import uvicorn

    # reload=False so the debugger attaches to this process and breakpoints work
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
    )
