from ...abc import ABCOutputData
from ..commons.task_data import TaskData


class TaskGetByIdOutputData(ABCOutputData):
    data: TaskData | None
