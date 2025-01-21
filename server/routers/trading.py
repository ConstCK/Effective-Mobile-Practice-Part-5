import json
import pickle
from typing import Annotated

from fastapi import APIRouter, status, Depends, Body

from crud.crud import TradingService
from services.services import Utils
from database.redis import TradingResultRepository
from schemas.trading import DatesOut, DatesRequest, DatesPeriod, TradingsFilter, \
    TradingsOut

# Маршрут для операций с торговыми данными
router = APIRouter(prefix='/api/v1/trading')
utils = Utils()


@router.get('/get_dates', description='Get latest trading dates',
            response_model=list[DatesOut],
            status_code=status.HTTP_200_OK, name='get_latest_trading_dates',
            responses={200: {'description': 'Успешное получение объектов'},
                       }
            )
async def get_latest_dates(db_service: Annotated[TradingService, Depends()],
                           number: Annotated[DatesRequest, Body()],
                           ):
    """Маршрут для получения указанного количества последних дат торгов биржи"""
    result = await db_service.get_last_trading_dates(number.number)
    return result


@router.get('/get_result_by_period', description='Get trading results by definite period',
            response_model=list[TradingsOut],
            status_code=status.HTTP_200_OK, name='get_trading_results_by_period',
            responses={200: {'description': 'Успешное получение объектов'},
                       }
            )
async def get_dynamics(db_service: Annotated[TradingService, Depends()],
                       period: Annotated[DatesPeriod, Body()],
                       cache: Annotated[TradingResultRepository, Depends()]):
    """Маршрут для получения результатов торгов биржи указанного периода"""

    # Формирования ключа для кэширования данных/получения данных из кэша
    key = utils.set_key_by_date(period)
    if await cache.key_exists(key):
        # Представление данных из кэша
        print('Getting cached data...')
        result = await cache.get_data(key)
    else:
        print('Getting data from DB...')
        # Представление данных из БД
        result = await db_service.get_tradings_by_period(period)
        # Приведение к строке для отправки в кэш
        data_for_cache = [TradingsOut(id=i.id,
                                      oil_id=i.oil_id,
                                      delivery_type_id=i.delivery_type_id,
                                      delivery_basis_id=i.delivery_basis_id).model_dump_json()
                          for i in result]
        # Добавление списка с данными (строками, полученными из объектов моделей схем) в кэш
        await cache.set_data(key, data_for_cache)
    return result


@router.get('/get_filtered_result', description='Get trading results by definite criteria',
            response_model=list[TradingsOut],
            status_code=status.HTTP_200_OK, name='get_trading_results_by_filter',
            responses={200: {'description': 'Успешное получение объектов'},
                       }
            )
async def get_trading_results(service: Annotated[TradingService, Depends()],
                              criteria: Annotated[TradingsFilter, Body()],
                              cache: Annotated[TradingResultRepository, Depends()]):
    """Маршрут для получения результатов торгов биржи с указанными критериями
     фильтрации запроса"""
    # Формирования ключа для кэширования данных/получения данных из кэша
    key = utils.set_key_by_criteria(criteria)
    if await cache.key_exists(key):
        # Представление данных из кэша
        print('Getting cached data...')
        result = await cache.get_data(key)
    else:
        print('Getting data from DB...')
        # Представление данных из БД
        result = await service.get_filtered_tradings(criteria)
        # Приведение к строке для отправки в кэш
        data_for_cache = [TradingsOut(id=i.id,
                                      oil_id=i.oil_id,
                                      delivery_type_id=i.delivery_type_id,
                                      delivery_basis_id=i.delivery_basis_id).model_dump_json()
                          for i in result]
        # Добавление списка с данными (строками, полученными из объектов моделей схем) в кэш
        await cache.set_data(key, data_for_cache)

    return result
