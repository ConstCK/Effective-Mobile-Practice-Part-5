import asyncio
from asyncio import get_event_loop

import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy import insert

from database.db import Base, test_engine, test_session
from database.redis import TradingResultRepository
from main import app
from models.trading import TradingResult
from tests.constants import INITIAL_DATA

red = TradingResultRepository()


# Создание стартовой фикстуры для удаления/создания таблиц в БД и наполнение их начальными данными
@pytest_asyncio.fixture
async def initial_run():
    await red.clear_cache()
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        await conn.execute(insert(TradingResult).values(INITIAL_DATA))
        await conn.commit()


# Создание фикстуры для использования клиента для запросов по маршрутам приложения
@pytest_asyncio.fixture(autouse=True, scope='session')
async def client():
    return AsyncClient(transport=ASGITransport(app=app), base_url='http://localhost')


# Создание фикстуры для использования единого Even Loop для всех тестов
@pytest.fixture(scope="module")
def event_loop():
    loop = get_event_loop()
    yield loop
