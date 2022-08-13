from pydantic import StrictStr

from ..base_response import BaseResponse


class HealthzGetResponse(BaseResponse):
    message: StrictStr = "OK"
