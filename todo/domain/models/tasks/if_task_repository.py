import abc

from ....interface import Interface
from .task import Task
from .task_id import TaskId


class IFTaskRepository(Interface):
    @abc.abstractmethod
    def find_by_id(self, task_id: TaskId) -> Task | None:
        ...

    @abc.abstractmethod
    def save(self, task: Task) -> None:
        ...

    @abc.abstractmethod
    def delete(self, task_id: TaskId) -> None:
        ...
