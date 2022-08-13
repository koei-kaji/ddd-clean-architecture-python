from pydantic import StrictStr

from ...abc import ABCInputData


class TaskDeleteInputData(ABCInputData):
    task_id: StrictStr
