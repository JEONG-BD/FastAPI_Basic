from fastapi import FastAPI
from todo.todo import todo_router 
# app = FastAPI()
app = FastAPI()

@app. get("/")
async def welcome() -> dict:
    return {"message": "Helo World"}

# uvicorn api:app --port 8000 --reload
# curl http://localhost:8000/

app.include_router(todo_router)

