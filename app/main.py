from enum import Enum

from fastapi import FastAPI
from api.routes.todo import todo_router
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI(
    title="MonsterTodoAPI",
    description="Ma première API avec fastAPI, c'est une dinguerie !",
    version="0.1.0",
)
app.include_router(todo_router)

register_tortoise(
    app,
    db_url="sqlite://todo.db",
	add_exception_handlers=True,
	generate_schemas=True,
    modules={"models": ["api.models.todo"]},
)