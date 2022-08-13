import abc

from pydantic import BaseModel

from custom_pydantic.config import BaseFrozenConfig


class ABCInputData(BaseModel, abc.ABC):
    class Config(BaseFrozenConfig):
        ...
