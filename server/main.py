from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn

from config import settings

from routers.trading import router as trading_router
from services.initial_tasks import init_models


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Создание события при запуске (и остановке) сервера (если нужно)
    """
    print('starting up server ...')
    await init_models()
    yield
    print('shutting down server connection...')


# Создание основного приложения
app = FastAPI(
    title='Trading exchange',
    description='For Effective Mobile practical training',
    lifespan=lifespan
)

# Включение маршрутов в основное приложение
app.include_router(trading_router, tags=['trading'])


# Приветственный маршрут
@app.get('/', description='Приветственная надпись', )
async def greetings() -> dict:
    return {'message': 'Greetings from Effective Mobile...'}


# Запуск сервера
if __name__ == '__main__':
    uvicorn.run('main:app', host=settings.host, port=8000, reload=True)
