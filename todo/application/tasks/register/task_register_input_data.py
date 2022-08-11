from pydantic import StrictStr

from ...abc import ABCInputData


class TaskRegisterInputData(ABCInputData):
    name: StrictStr
