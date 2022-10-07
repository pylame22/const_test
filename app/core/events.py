from typing import Callable

from fastapi import FastAPI

from core.database import database


def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app():
        await database.connect()

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    async def stop_app():
        await database.disconnect()

    return stop_app
