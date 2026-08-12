import sqlite3
from fastapi import Response
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

DATABASE = "tasks.db"

app = FastAPI(title="Basic FastAPI Server")


class TaskCreate(BaseModel):
    title: str
    done: bool


def init_database():
    connection = sqlite3.connect(DATABASE)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            done BOOLEAN NOT NULL
        )
    """)

    connection.commit()

    existing_tasks = connection.execute(
        "SELECT COUNT(*) FROM tasks"
    ).fetchone()[0]

    if existing_tasks == 0:
        connection.executemany(
            "INSERT INTO tasks (id, title, done) VALUES (?, ?, ?)",
            [
                (1, "Learn FastAPI", False),
                (2, "Build Task API", False),
                (3, "Test Task API", True)
            ]
        )
        connection.commit()

    connection.close()

init_database()

@app.get("/", description="Get basic information about the Task API.")
def read_root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }


@app.get("/health", description="Check whether the API is running.")
def health_check():
    return {"status": "ok"}


@app.get("/tasks", description="Get all tasks.")
def get_tasks():
    connection = sqlite3.connect(DATABASE)

    rows = connection.execute(
        "SELECT id, title, done FROM tasks"
    ).fetchall()

    connection.close()

    return [
        {
            "id": row[0],
            "title": row[1],
            "done": bool(row[2])
        }
        for row in rows
    ]


@app.get("/tasks/{id}", description="Get a single task by ID.")
def get_task(id: int):
    connection = sqlite3.connect(DATABASE)

    row = connection.execute(
        "SELECT id, title, done FROM tasks WHERE id = ?",
        (id,)
    ).fetchone()

    connection.close()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail=f"Task {id} not found"
        )

    return {
        "id": row[0],
        "title": row[1],
        "done": bool(row[2])
    }


@app.post("/tasks", status_code=201, description="Create a new task.")
def create_task(task: TaskCreate):
    connection = sqlite3.connect(DATABASE)

    cursor = connection.execute(
        "INSERT INTO tasks (title, done) VALUES (?, ?)",
        (task.title, task.done)
    )

    connection.commit()

    new_id = cursor.lastrowid

    connection.close()

    return {
        "id": new_id,
        "title": task.title,
        "done": task.done
    }

@app.put("/tasks/{id}", description="Update an existing task by ID.")
def update_task(id: int, task: TaskCreate):
    connection = sqlite3.connect(DATABASE)

    cursor = connection.execute(
        "UPDATE tasks SET title = ?, done = ? WHERE id = ?",
        (task.title, task.done, id)
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()
        raise HTTPException(
            status_code=404,
            detail=f"Task {id} not found"
        )

    row = connection.execute(
        "SELECT id, title, done FROM tasks WHERE id = ?",
        (id,)
    ).fetchone()

    connection.close()

    return {
        "id": row[0],
        "title": row[1],
        "done": bool(row[2])
    }

@app.delete("/tasks/{id}", status_code=204, description="Delete a task by ID.")
def delete_task(id: int):
    connection = sqlite3.connect(DATABASE)

    cursor = connection.execute(
        "DELETE FROM tasks WHERE id = ?",
        (id,)
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()
        raise HTTPException(
            status_code=404,
            detail=f"Task {id} not found"
        )

    connection.close()

    return Response(status_code=204)