from fastapi import FastAPI 
from todo.todo import todo_router 
# app = FastAPI()
app = FastAPI()

app.include_router(todo_router)

