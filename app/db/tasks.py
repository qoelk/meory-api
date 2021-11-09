from databases import Database
from fastapi import FastAPI
import logging

from app.core.config import DATABASE_URL

logger = logging.getLogger(__name__)


async def db_connect(app: FastAPI) -> None:
    db = Database(DATABASE_URL)
    try:
        await db.connect()
        app.state.db = db
    except Exception as e:
        logger.warning('DATABASE CONNECTION ERROR')


async def db_disconnect(app: FastAPI) -> None:
    try:
        await app.state.db.disconnect()
    except Exception as e:
        logger.warning('FAILED TO DISCONNECT')
