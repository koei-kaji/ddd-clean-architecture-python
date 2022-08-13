from uuid import uuid4

from ....domain.models.tasks import IFTaskFactory, Task, TaskId, TaskName, TaskStatus


class InMemoryTaskFactory(IFTaskFactory):
    def create(self, name: TaskName) -> Task:
        task_id = TaskId(value=str(uuid4()))
        return Task(task_id=task_id, name=name, status=TaskStatus.TODO)
