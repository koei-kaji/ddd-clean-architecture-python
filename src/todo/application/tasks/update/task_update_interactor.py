from typing import Any, cast

from injector import inject, singleton
from pydantic import PrivateAttr

from ....domain.models.tasks import IFTaskRepository, TaskId, TaskName
from ...abc import ABCInputData, ABCInteractor, ABCOutputData
from ..commons.task_status import TaskStatus
from .task_update_input_data import TaskUpdateInputData
from .task_update_output_data import TaskUpdateOutputData


@singleton
class TaskUpdateInteractor(ABCInteractor):
    __task_repository: IFTaskRepository = PrivateAttr()

    @inject
    def __init__(
        self,
        task_repository: IFTaskRepository,
        **data: Any,
    ) -> None:
        super().__init__(**data)
        self.__task_repository = task_repository

    def handle(self, input_data: ABCInputData) -> ABCOutputData:
        input_data = cast(TaskUpdateInputData, input_data)

        task_id = TaskId(value=input_data.task_id)
        task = self.__task_repository.find_by_id(task_id)
        if task is None:
            # TODO: use custom exception
            # pylint: disable=broad-exception-raised
            raise Exception(f"Task's id {input_data.task_id} was not found")
            # pylint: enable=broad-exception-raised

        if input_data.name is not None:
            name = TaskName(value=input_data.name)
            task.change_name(name)

        match input_data.status:
            case TaskStatus.TODO:
                task.change_status_to_todo()
            case TaskStatus.DONE:
                task.change_status_to_done()
            case None:
                pass
            case _:
                raise ValueError(f"Status {input_data.status} was not declared")

        self.__task_repository.save(task)

        return TaskUpdateOutputData()
