from ....application.tasks.commons.task_data import TaskData
from ....application.tasks.get_all import TaskGetAllInputData, TaskGetAllOutputData
from ....application.tasks.get_by_id import TaskGetByIdInputData, TaskGetByIdOutputData
from ....application.tasks.if_task_query_service import IFTaskQueryService
from .in_memory_data import data


class InMemoryTaskQueryService(IFTaskQueryService):
    def get_by_id(self, input_data: TaskGetByIdInputData) -> TaskGetByIdOutputData:
        task_tuple = data.get(input_data.task_id, None)
        if task_tuple is None:
            return TaskGetByIdOutputData(data=None)
        return TaskGetByIdOutputData(
            data=TaskData(
                task_id=input_data.task_id,
                name=task_tuple.name,
                status=task_tuple.status,
            )
        )

    def get_all(self, _: TaskGetAllInputData) -> TaskGetAllOutputData:
        output_data = [
            TaskData(task_id=key, name=value.name, status=value.status)
            for key, value in data.items()
        ]

        return TaskGetAllOutputData(data=output_data)
