from fastapi import FastAPI

app = FastAPI()

@app.get("/demo")
def read_demo():
    return {"message": "Hello from FastAPI!"}
