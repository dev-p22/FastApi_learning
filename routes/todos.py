from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database.database import get_db
from models.todo import TodoModel

router = APIRouter()


class Todo(BaseModel):
    title: str
    completed: bool = False


def todo_response(todo: TodoModel) -> dict:
    return {
        "id": todo.id,
        "title": todo.title,
        "completed": todo.completed,
    }


@router.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(TodoModel).all()
    return {"Success": True, "Data": [todo_response(todo) for todo in todos]}


@router.post("/todos", status_code=201)
def add_todo(todo: Todo, db: Session = Depends(get_db)):
    db_todo = TodoModel(title=todo.title, completed=todo.completed)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return {"Success": True, "Data": todo_response(db_todo)}


@router.get("/todos/{id}")
def get_todo(id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.id == id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo Not Found")
    return {"Success": True, "Data": todo_response(todo)}


@router.put("/todos/{id}")
def update_todo(id: int, updated_todo: Todo, db: Session = Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.id == id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo Not Found")

    todo.title = updated_todo.title
    todo.completed = updated_todo.completed
    db.commit()
    db.refresh(todo)
    return {"Success": True, "Data": todo_response(todo)}


@router.delete("/todos/{id}")
def delete_todo(id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.id == id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo Not Found")

    db.delete(todo)
    db.commit()
    return {"Success": True}
