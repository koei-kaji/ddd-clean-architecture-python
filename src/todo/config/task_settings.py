from enum import Enum, unique

from pydantic_settings import BaseSettings


@unique
class TaskAdapter(str, Enum):
    in_memory = "in_memory"


class TaskSettings(BaseSettings):
    task_adapter: TaskAdapter = TaskAdapter.in_memory
