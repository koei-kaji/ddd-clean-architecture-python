from typing import Any, cast

from injector import inject
from pydantic import PrivateAttr

from custom_pydantic.config import BaseFrozenConfig

from ....domain.models.tasks import IFTaskRepository, TaskId
from ...abc import ABCInputData, ABCInteractor, ABCOutputData
from .task_delete_input_data import TaskDeleteInputData
from .task_delete_output_data import TaskDeleteOutputData


class TaskDeleteInteractor(ABCInteractor):
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
        input_data = cast(TaskDeleteInputData, input_data)

        task_id = TaskId(value=input_data.task_id)
        self.__task_repository.delete(task_id)

        return TaskDeleteOutputData()

    class Config(BaseFrozenConfig):
        ...
