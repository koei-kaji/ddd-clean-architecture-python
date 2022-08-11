from __future__ import annotations

import abc
from typing import TYPE_CHECKING

from ...interface import Interface

if TYPE_CHECKING:
    from ..tasks.get_all import TaskGetAllInputData, TaskGetAllOutputData
    from ..tasks.get_by_id import TaskGetByIdInputData, TaskGetByIdOutputData


class IFTaskQueryService(Interface):
    @abc.abstractmethod
    def get_by_id(self, input_data: TaskGetByIdInputData) -> TaskGetByIdOutputData:
        ...

    @abc.abstractmethod
    def get_all(self, input_data: TaskGetAllInputData) -> TaskGetAllOutputData:
        ...
