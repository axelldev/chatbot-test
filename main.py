from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Chatbot API is running"}


@app.get("/health")
async def health():
    return {"status": "healthy"}
