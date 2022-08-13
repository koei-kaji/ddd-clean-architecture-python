from ...abc import ABCOutputData
from ..commons.task_data import TaskData


class TaskRegisterOutputData(ABCOutputData):
    data: TaskData
