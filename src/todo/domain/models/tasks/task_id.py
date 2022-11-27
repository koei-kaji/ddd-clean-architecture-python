from __future__ import annotations

from pydantic import StrictStr

from ..base_model import ValueObjectModel


class TaskId(ValueObjectModel):
    value: StrictStr
