import abc

from custom_pydantic.model import ABCBaseFrozenModel

from .abc_input_data import ABCInputData
from .abc_output_data import ABCOutputData


class ABCInteractor(ABCBaseFrozenModel):
    @abc.abstractmethod
    def handle(self, input_data: ABCInputData) -> ABCOutputData:
        ...
