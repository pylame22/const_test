from fastapi import APIRouter
from pydantic import HttpUrl

from schemas.link import LinkResponse, LinkCreate, LinkDelete
from services.link import create_short_link, get_full_link, delete_link

router = APIRouter()


@router.post(
    '/link/',
    response_model=LinkResponse,
)
async def create_short_link_api(
        schema: LinkCreate,
) -> LinkResponse:
    return await create_short_link(schema)


@router.get(
    '/link/',
    response_model=LinkResponse,
    responses={404: {}},
)
async def get_full_link_api(
        url: HttpUrl,
) -> LinkResponse:
    return await get_full_link(url)


@router.delete(
    '/link/',
)
async def delete_link_api(
        schema: LinkDelete,
):
    return await delete_link(schema)
