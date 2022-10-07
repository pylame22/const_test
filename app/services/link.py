from fastapi import HTTPException, status
from pydantic import HttpUrl
from sqlalchemy import select, exists

from core.database import database
from schemas.link import LinkResponse, LinkCreate, LinkDelete
from tables import link_table
from .shortify import shortify_link


async def _create_short_link(full_link: HttpUrl) -> str:
    url = full_link
    short_link = None
    while short_link is None:
        url = shortify_link(url)
        q = exists(
            select([1]).select_from(link_table).where(link_table.c.short_link == url)
        ).select()
        if not await database.fetch_val(q):
            short_link = url
    return short_link


async def create_short_link(schema: LinkCreate) -> LinkResponse:
    async with database.transaction():
        q = select([link_table.c.short_link]) \
            .select_from(link_table) \
            .where(link_table.c.full_link == schema.url)
        short_link = await database.fetch_val(q)
        if not short_link:
            short_link = await _create_short_link(schema.url)
            q = link_table.insert() \
                .values(short_link=short_link, full_link=schema.url)
            await database.execute(q)
    return LinkResponse.construct(url=short_link)


async def get_full_link(short_link: HttpUrl) -> LinkResponse:
    q = select([link_table.c.full_link]) \
        .select_from(link_table) \
        .where(link_table.c.short_link == short_link)
    full_link = await database.fetch_val(q)
    if not full_link:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return LinkResponse.construct(url=full_link)


async def delete_link(schema: LinkDelete):
    q = link_table.delete() \
        .where(link_table.c.short_link == schema.url)
    await database.execute(q)
