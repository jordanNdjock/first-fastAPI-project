from tortoise.models import Model
from tortoise.fields import CharField, BooleanField, IntField, DatetimeField, UUIDField

class Todo(Model):
    id = UUIDField(pk=True)
    title = CharField(max_length=100, null=False)
    description = CharField(max_length=255, null=True)
    completed = BooleanField(default=False, null=False)
    created_at = DatetimeField(auto_now_add=True, null=False)