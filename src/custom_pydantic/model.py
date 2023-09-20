import abc

from pydantic import BaseModel as PydanticBaseModel

from . import config


class ABCBaseFrozenModel(PydanticBaseModel, abc.ABC):
    model_config = config.BaseFrozenConfigDict


class BaseModel(PydanticBaseModel):
    model_config = config.BaseConfigDict


class BaseFrozenModel(PydanticBaseModel):
    model_config = config.BaseFrozenConfigDict
