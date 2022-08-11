from pydantic import StrictStr

from ...abc import ABCInputData


class TaskGetByIdInputData(ABCInputData):
    task_id: StrictStr
