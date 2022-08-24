from typing import Any, cast

from injector import inject, singleton
from pydantic import PrivateAttr

from custom_pydantic.config import BaseFrozenConfig

from ...abc import ABCInputData, ABCInteractor, ABCOutputData
from ..if_task_query_service import IFTaskQueryService
from .task_get_by_id_input_data import TaskGetByIdInputData


@singleton
class TaskGetByIdInteractor(ABCInteractor):
    __task_query_service: IFTaskQueryService = PrivateAttr()

    @inject
    def __init__(
        self,
        task_query_service: IFTaskQueryService,
        **data: Any,
    ) -> None:
        super().__init__(**data)
        self.__task_query_service = task_query_service

    def handle(self, input_data: ABCInputData) -> ABCOutputData:
        input_data = cast(TaskGetByIdInputData, input_data)

        return self.__task_query_service.get_by_id(input_data)

    class Config(BaseFrozenConfig):
        ...
