from pydantic import HttpUrl

from core.schemas import JSONBaseModel


class LinkCreate(JSONBaseModel):
    url: HttpUrl


class LinkResponse(JSONBaseModel):
    url: HttpUrl


class LinkDelete(JSONBaseModel):
    url: HttpUrl

