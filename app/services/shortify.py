import base64
import hashlib

from core.settings import SHORT_HOST


def shortify_link(value: str) -> str:
    return SHORT_HOST + base64.b64encode(hashlib.md5(value.encode('utf-8')).digest()).decode('utf-8')[:4]
