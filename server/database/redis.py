import json
import os
import pickle
from typing import Any

from config import settings
from redis import asyncio as aioredis
from schemas.trading import TradingsOut


class TradingResultRepository:
    """
    Класс для кэширования данных торговой биржи
    """

    def __init__(self) -> None:
        self.red = aioredis.from_url(settings.redis_url, encoding='utf8',
                                     decode_responses=True)

    # Добавление данных в кэш
    async def set_data(self, key: str, items: list[Any], expire_time: int) -> None:
        for i in items:
            # Добавление строки в кэш к списку с указанным ключом
            await self.red.rpush(key, i)
        await self.red.expire(key, expire_time)

    # Получение данных из кэша
    async def get_data(self, key: str) -> list[TradingsOut] | Any:
        # Возвращает список элементов с 0 индекса до последнего включительно
        data = await self.red.lrange(key, 0, -1)
        if data:
            return [json.loads(i) for i in data]
        return []

    # Получение всех ключей БД
    async def show_all_keys(self):
        return await self.red.keys()

    # Проверка ключа на существовании в кэше
    async def key_exists(self, key: str) -> bool:
        return await self.red.exists(key)

    # Очистка кэша
    async def clear_cache(self):
        await self.red.flushall()
