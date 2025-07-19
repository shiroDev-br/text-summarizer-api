from fastapi import FastAPI

def setup():
    app = FastAPI(
        title="TextSummarizer API",
        description="An api that summarizes long texts contained in files",
        version="0.1.0"
    )

    @app.get("/")
    async def read_main():
        return {"msg": "Hello World"}
    