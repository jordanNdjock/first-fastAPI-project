from fastapi import APIRouter, HTTPException, status
from api.models.todo import Todo
from api.schemas.todo import getTodo, PostTodo, PutTodo, CompleteTodo

todo_router = APIRouter(prefix="/todos", tags=["Todos"])

@todo_router.get("/")
async def all_todos():
	data = Todo.all()
	return await getTodo.from_queryset(data)

@todo_router.post("/")
async def create_todo(body: PostTodo):
	row = await Todo.create(**body.model_dump(exclude_unset=True))
	return await getTodo.from_tortoise_orm(row)

@todo_router.get("/{todo_id}")
async def get_todo(todo_id: str):
	exists = await Todo.filter(id=todo_id).exists()
	if not exists:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
	return await getTodo.from_queryset_single(Todo.get(id=todo_id))

@todo_router.patch("/complete/{todo_id}")
async def complete_todo(todo_id: str, body: CompleteTodo):
	data = body.model_dump(exclude_unset=True)
	exists = await Todo.filter(id=todo_id).exists()
	if not exists:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
	await Todo.filter(id=todo_id).update(**data)
	return await getTodo.from_queryset_single(Todo.get(id=todo_id))

@todo_router.put("/{todo_id}")
async def update_todo(todo_id: str, body: PutTodo):
	data = body.model_dump(exclude_unset=True)
	exists = await Todo.filter(id=todo_id).exists()
	if not exists:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
	await Todo.filter(id=todo_id).update(**data)
	return await getTodo.from_queryset_single(Todo.get(id=todo_id))

@todo_router.delete("/{todo_id}")
async def delete_todo(todo_id: str):
	exists = await Todo.filter(id=todo_id).exists()
	if not exists:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
	await Todo.filter(id=todo_id).delete()
	return "Todo deleted successfully"