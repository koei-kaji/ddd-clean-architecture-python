from typing import List

from ...abc import ABCOutputData
from ..commons.task_data import TaskData


class TaskGetAllOutputData(ABCOutputData):
    data: List[TaskData]
