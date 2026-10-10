from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Title")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost', 'http://localhost:8000', 'http://127.0.0.1', 'http://127.0.0.1:8000'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/health')
async def check():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        loop="uvloop",
        host="127.0.0.1",
        port=8000,
    )
