import abc

from pydantic import BaseModel

from custom_pydantic.config import BaseFrozenConfig

from .abc_input_data import ABCInputData
from .abc_output_data import ABCOutputData


class ABCInteractor(BaseModel, abc.ABC):
    @abc.abstractmethod
    def handle(self, input_data: ABCInputData) -> ABCOutputData:
        ...

    class Config(BaseFrozenConfig):
        ...
