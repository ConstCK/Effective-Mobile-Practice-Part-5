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
@pytest_asyncio.fixture(scope='module')
async def initial_run():
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.execute(insert(TradingResult).values(INITIAL_DATA))
        await conn.commit()
    yield
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await red.clear_cache()


# Создание фикстуры для использования клиента для запросов по маршрутам приложения
@pytest_asyncio.fixture(scope='session')
async def client():
    return AsyncClient(transport=ASGITransport(app=app), base_url='http://localhost')


# Создание фикстуры для использования асинхронной сессии в CRUD методах
@pytest_asyncio.fixture(scope='function')
async def session():
    async with test_session() as session:
        try:
            yield session
        finally:
            await session.close()


# Создание фикстуры для использования единого Even Loop для всех тестов
@pytest_asyncio.fixture(scope="session")
def event_loop():
    loop = get_event_loop()
    yield loop
