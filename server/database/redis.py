import os
from typing import Any

from config import settings
from redis import asyncio as aioredis


class TradingResultRepository:
    """
    Класс для кэширования данных торговой биржи
    """

    def __init__(self) -> None:
        self.red = aioredis.from_url(f"redis://{settings.redis_url}:6379/0", encoding='utf8',
                                     decode_responses=True)

    # Добавление данных в кэш
    async def set_data(self, key: str, item: dict[str, Any], expire_time: int) -> None:
        await self.red.set(key, item, expire_time)

    # Получение данных из кэша
    async def get_token(self, key: str) -> dict[str: Any] | None:
        result = await self.red.get(key)
        return result
