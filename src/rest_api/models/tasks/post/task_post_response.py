from pydantic import StrictStr

from ...base_response import BaseResponse


class TaskPostResponse(BaseResponse):
    id: StrictStr
    name: StrictStr
    status: StrictStr
