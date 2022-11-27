from ..base_model import EntityModel
from .task_id import TaskId
from .task_name import TaskName
from .task_status import TaskStatus


class Task(EntityModel):
    task_id: TaskId
    name: TaskName
    status: TaskStatus

    def change_name(self, name: TaskName) -> None:
        self.name = name

    def change_status_to_todo(self) -> None:
        self.status = TaskStatus.TODO

    def change_status_to_done(self) -> None:
        self.status = TaskStatus.DONE
