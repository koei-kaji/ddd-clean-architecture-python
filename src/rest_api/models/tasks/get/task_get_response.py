from typing import List

from pydantic import StrictStr

from ...base_response import BaseResponse


class TaskGetResponse(BaseResponse):
    id: StrictStr
    name: StrictStr
    status: StrictStr


class TaskGetAllResponse(BaseResponse):
    data: List[TaskGetResponse]
