from pydantic import BaseModel

from custom_pydantic.config import BaseConfig

from .task_id import TaskId
from .task_name import TaskName
from .task_status import TaskStatus


class Task(BaseModel):
    task_id: TaskId
    name: TaskName
    status: TaskStatus

    class Config(BaseConfig):
        ...

    def change_name(self, name: TaskName) -> None:
        self.name = name

    def change_status_to_todo(self) -> None:
        self.status = TaskStatus.TODO

    def change_status_to_done(self) -> None:
        self.status = TaskStatus.DONE
