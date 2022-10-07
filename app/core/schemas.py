import orjson

from pydantic import BaseModel


def _orjson_dumps(*args, **kwargs):
    return orjson.dumps(*args, **kwargs).decode()


class JSONBaseModel(BaseModel):
    class Config:
        json_dumps = _orjson_dumps
        json_loads = orjson.loads
