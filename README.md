# Task API

A simple RESTful Task API built with **FastAPI** and **Python** as a backend engineering learning project.

The API demonstrates the core CRUD operations:

- **Create** tasks with `POST`
- **Read** tasks with `GET`
- **Update** tasks with `PUT`
- **Delete** tasks with `DELETE`

The project uses an in-memory Python list for task storage, so data is reset whenever the server restarts.

## Requirements

- Python 3.12+
- Git
- Windows PowerShell (commands below use `curl.exe`)

## Installation & Run

Clone the repository, enter the project directory, and run the following command:

```powershell
python -m pip install -r requirements.txt; .venv\Scripts\uvicorn.exe main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

> If your repository does not contain a `requirements.txt`, install the project dependencies in the virtual environment first (for example, FastAPI and Uvicorn), then run the Uvicorn command above.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Returns API information and available endpoints |
| GET | `/health` | Checks whether the API is running |
| GET | `/tasks` | Returns all tasks |
| GET | `/tasks/{id}` | Returns a single task by ID |
| POST | `/tasks` | Creates a new task |
| PUT | `/tasks/{id}` | Updates an existing task |
| DELETE | `/tasks/{id}` | Deletes a task |

### Task object

A task contains:

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "done": false
}
```

For task creation/update requests, the server manages the task ID.

## Example `curl -i` Output

Example from the running API:

```text
PS D:\task-api> curl.exe -i http://127.0.0.1:8000/tasks

HTTP/1.1 200 OK
date: Tue, 11 Aug 2026 05:44:24 GMT
server: uvicorn
content-length: 139
content-type: application/json

[{"id":1,"title":"Learn FastAPI","done":false},{"id":2,"title":"Build Task API","done":false},{"id":3,"title":"Test Task API","done":true}]
```

## Swagger UI

The API can also be tested interactively through FastAPI's automatically generated Swagger UI.

Open:

```text
http://127.0.0.1:8000/docs
```

Add the Swagger screenshot to this README after capturing it:

```markdown
![Swagger UI](docs/swagger.png)
```

Recommended repository structure:

```text
task-api/
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
└── docs/
    └── swagger.png
```

## Project Notes

This project was built incrementally through multiple stages, with each stage committed to Git. The stages progressed from a basic FastAPI server to health checking, task retrieval, task creation, task updating, task deletion, and finally CRUD testing through Swagger UI.

The application currently uses in-memory storage rather than a database. This keeps the project focused on understanding HTTP methods, FastAPI routing, request validation, response status codes, and CRUD API behavior.

## Running the API in Under 5 Minutes

1. Clone the public GitHub repository.
2. Install the Python dependencies.
3. Start the Uvicorn server using the command above.
4. Open `http://127.0.0.1:8000/docs`.
5. Use Swagger UI to test the CRUD endpoints.

