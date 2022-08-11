from pydantic import StrictStr

from ...base_request import BaseRequest


class TaskDeleteRequest(BaseRequest):
    id: StrictStr
