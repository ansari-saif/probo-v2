from fastapi import HTTPException
from sqlmodel import Session, select
from app.models.todo import Todo, TodoCreate, TodoUpdate

def create_todo_service(todo_data: TodoCreate, session: Session):
    todo = Todo.from_orm(todo_data)
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

def get_todo_service(todo_id: int, session: Session):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

# Update Todo service
def update_todo_service(todo_id: int, todo_data: TodoUpdate, session: Session):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    for key, value in todo_data.dict(exclude_unset=True).items():
        setattr(todo, key, value)
    
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

# Delete Todo service
def delete_todo_service(todo_id: int, session: Session):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    session.delete(todo)
    session.commit()

# List All Todos service
def list_all_todos_service(session: Session):
    todos = session.exec(select(Todo)).all()
    return todos