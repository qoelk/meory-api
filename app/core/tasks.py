from typing import Callable

from fastapi import FastAPI

from app.db.tasks import db_disconnect, db_connect


def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        await db_connect(app)

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        await db_disconnect(app)

    return stop_app
