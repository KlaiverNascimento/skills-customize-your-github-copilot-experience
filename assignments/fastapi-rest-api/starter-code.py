from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str
    description: str


class Task(TaskCreate):
    id: int
    completed: bool = False


tasks: dict[int, Task] = {}


def get_task_or_404(task_id: int) -> Task:
    """Return a task or raise HTTP 404 when it does not exist."""
    # TODO: Find the task and raise HTTPException if it is missing.
    raise NotImplementedError


@app.get("/tasks", response_model=list[Task])
def list_tasks() -> list[Task]:
    # TODO: Return all tasks.
    raise NotImplementedError


@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int) -> Task:
    # TODO: Return the requested task.
    raise NotImplementedError


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate) -> Task:
    # TODO: Assign a unique ID, create the task, store it, and return it.
    raise NotImplementedError


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_data: TaskCreate) -> Task:
    # TODO: Replace the task's title and description, preserving its ID.
    raise NotImplementedError


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> None:
    # TODO: Remove the task. Return no body on success.
    raise NotImplementedError
