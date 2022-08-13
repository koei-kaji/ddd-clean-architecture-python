import abc

from pydantic import BaseModel

from custom_pydantic.config import BaseFrozenConfig


class ABCOutputData(BaseModel, abc.ABC):
    class Config(BaseFrozenConfig):
        ...
