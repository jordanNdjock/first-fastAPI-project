from pydantic import BaseModel, Field
from tortoise.contrib.pydantic import pydantic_model_creator
from api.models.todo import Todo

getTodo = pydantic_model_creator(Todo, name="Todo")

class PostTodo(BaseModel):
	title: str = Field(..., description="The title of the task")
	description: str | None = Field(None, description="The description of the task")
	completed: bool

class PutTodo(BaseModel):
	title: str | None = Field(None, max_length=100)
	description: str | None = Field(None, description="The description of the task")
	completed: bool | None

class CompleteTodo(BaseModel):
	completed: bool 