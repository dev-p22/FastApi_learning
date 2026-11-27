from fastapi import APIRouter,HTTPException
from pydantic import BaseModel

router = APIRouter()

todos = []

#custom exceptions
class TodosNotFoundEXception(Exception):
    def __init__(self, name :str):
        self.name = name

class Todo(BaseModel):
    id : int
    title : str
    completed : bool = False

@router.get("/todos")
def get_todos():
    return {"Data":todos}

@router.post("/todos")
def add_todos(todo : Todo):
    todos.append(todo)
    return { "Success" : True , "Data" : todo}

@router.get("/todos/{id}")
def get_todo(id : int):
    for todo in todos:
        if todo.id == id:
            return todo
    raise HTTPException(status_code=404 , detail="Todo Not Found")

@router.put("/todos/{id}")
def update_todo(id:int,updated_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id == id:
            todos[index] = updated_todo
            return {"success" : True , "Data" : updated_todo}
    return {"Error":"Todo Not Found"}


@router.delete("/todos/{id}")
def delete_todo(id:int):
    for index,todo in enumerate(todos):
        if(todo.id) == id:
            todos.pop(index)
            return {"Success": True}        