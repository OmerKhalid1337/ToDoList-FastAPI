from fastapi import FastAPI

app = FastAPI(title="Basic FastAPI Server")

@app.get("/")
def read_root():
    return {"message": "Hello World. The environment is successfully validated and running."}
