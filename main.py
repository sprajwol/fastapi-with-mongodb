from fastapi import FastAPI

app = FastAPI()


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to the project!"
    }
