from pydantic import StrictStr

from ...base_request import BaseRequest


class TaskPostRequest(BaseRequest):
    name: StrictStr
