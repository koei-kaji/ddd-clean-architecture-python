import abc

from ....interface import Interface
from .task import Task
from .task_name import TaskName


class IFTaskFactory(Interface):
    @abc.abstractmethod
    def create(self, name: TaskName) -> Task:
        pass
