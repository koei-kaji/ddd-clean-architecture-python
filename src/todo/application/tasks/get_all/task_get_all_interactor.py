from typing import Any, cast

from injector import inject, singleton
from pydantic import PrivateAttr

from ...abc import ABCInputData, ABCInteractor, ABCOutputData
from ..if_task_query_service import IFTaskQueryService
from .task_get_all_input_data import TaskGetAllInputData


@singleton
class TaskGetAllInteractor(ABCInteractor):
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
        input_data = cast(TaskGetAllInputData, input_data)
        return self.__task_query_service.get_all(input_data)
