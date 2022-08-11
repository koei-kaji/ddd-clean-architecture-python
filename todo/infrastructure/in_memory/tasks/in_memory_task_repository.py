from ....domain.models.tasks import IFTaskRepository, Task, TaskId, TaskName, TaskStatus
from .in_memory_data import TaskTuple, data


class InMemoryTaskRepository(IFTaskRepository):
    def find_by_id(self, task_id: TaskId) -> Task | None:
        task_tuple = data.get(task_id.value, None)
        if task_tuple is None:
            return None
        return Task(
            task_id=task_id,
            name=TaskName(value=task_tuple.name),
            status=TaskStatus(task_tuple.status),
        )

    def save(self, task: Task) -> None:
        data[task.task_id.value] = TaskTuple(
            name=task.name.value, status=task.status.value
        )

    def delete(self, task_id: TaskId) -> None:
        data.pop(task_id.value, None)
