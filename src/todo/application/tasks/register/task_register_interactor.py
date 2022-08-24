from typing import Any, cast

from injector import inject, singleton
from pydantic import PrivateAttr

from custom_pydantic.config import BaseFrozenConfig

from ....domain.models.tasks import IFTaskFactory, IFTaskRepository, TaskName
from ...abc import ABCInputData, ABCInteractor, ABCOutputData
from ..commons.task_data import TaskData
from .task_register_input_data import TaskRegisterInputData
from .task_register_output_data import TaskRegisterOutputData


@singleton
class TaskRegisterInteractor(ABCInteractor):
    __task_factory: IFTaskFactory = PrivateAttr()
    __task_repository: IFTaskRepository = PrivateAttr()

    @inject
    def __init__(
        self,
        task_factory: IFTaskFactory,
        task_repository: IFTaskRepository,
        **data: Any,
    ) -> None:
        super().__init__(**data)
        self.__task_factory = task_factory
        self.__task_repository = task_repository

    def handle(self, input_data: ABCInputData) -> ABCOutputData:
        input_data = cast(TaskRegisterInputData, input_data)

        name = TaskName(value=input_data.name)
        task = self.__task_factory.create(name)
        self.__task_repository.save(task)

        return TaskRegisterOutputData(
            data=TaskData(
                task_id=task.task_id.value,
                name=task.name.value,
                status=task.status.value,
            )
        )

    class Config(BaseFrozenConfig):
        ...
