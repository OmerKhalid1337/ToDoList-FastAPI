from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Basic FastAPI Server")


class TaskCreate(BaseModel):
    title: str
    done: bool


tasks = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "done": False
    },
    {
        "id": 2,
        "title": "Build Task API",
        "done": False
    },
    {
        "id": 3,
        "title": "Test Task API",
        "done": True
    }
]


@app.get("/")
def read_root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{id}")
def get_task(id: int):
    for task in tasks:
        if task["id"] == id:
            return task

    raise HTTPException(
        status_code=404,
        detail=f"Task {id} not found"
    )


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    new_id = max((int(existing_task["id"]) for existing_task in tasks), default=0) + 1

    new_task = {
        "id": new_id,
        "title": task.title,
        "done": task.done
    }

    tasks.append(new_task)

    return new_task