# Создание таблиц в БД при запуске приложения
from database.db import engine, Base


async def init_models() -> None:
    """
    Создание моделей в БД при запуске сервера при их отсутствии
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
