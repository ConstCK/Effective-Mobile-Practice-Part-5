import pytest

from fastapi import status
from pydantic import ValidationError

from crud.crud import TradingService

from main import app
from schemas.trading import DatesPeriod, TradingsFilter
from tests.constants import PERIOD_REQUEST_1, PERIOD_REQUEST_2, DATES_REQUEST_1, DATES_REQUEST_2, DATES_REQUEST_3, \
    CRITERIA_REQUEST_1, CRITERIA_REQUEST_2, CRITERIA_REQUEST_3, CRITERIA_REQUEST_4, CRITERIA_REQUEST_5


# Тест функции для получения дат
@pytest.mark.asyncio
async def test_get_last_trading_dates(session):
    service = TradingService(session)
    response = await service.get_last_trading_dates(dates_number=1)
    assert len(response) == 1


# Тест функции для получения данных торгов в указанный период
@pytest.mark.asyncio
async def test_get_tradings_by_period(session):
    service = TradingService(session)
    response = await service.get_tradings_by_period(period=DatesPeriod.model_validate(PERIOD_REQUEST_1)
                                                    )
    assert len(response) == 2


# Тест функции для получения результатов торгов с указанными критериями
@pytest.mark.asyncio
async def test_get_filtered_tradings(session):
    service = TradingService(session)
    response = await service.get_filtered_tradings(criteria=TradingsFilter.model_validate(CRITERIA_REQUEST_2))

    assert len(response) == 2

# Тест функции для получения результатов торгов с некорректными критериями
@pytest.mark.asyncio
async def test_get_filtered_tradings(session):
    service = TradingService(session)
    with pytest.raises(ValidationError):
        await service.get_filtered_tradings(criteria=TradingsFilter.model_validate('Wrong type of data'))


# Тест маршрута для получения последних дат торгов
@pytest.mark.asyncio
@pytest.mark.parametrize('number, expected', [
    (DATES_REQUEST_1, 2),
    (DATES_REQUEST_2, 5),
    (DATES_REQUEST_3, 5),
])
async def test_getting_dates(client, number, expected):
    response = await client.post('/api/v1/trading/get_dates',
                                 json=number)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == expected


# Тест маршрута для получения результатов торгов в указанный период
@pytest.mark.asyncio
@pytest.mark.parametrize('dates, expected', [
    (PERIOD_REQUEST_1, 2),
    (PERIOD_REQUEST_2, 5),
])
async def test_getting_results_by_period(client, dates, expected):
    response = await client.post('/api/v1/trading/get_result_by_period',
                                 json=dates)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == expected


# Тест маршрута для получения результатов торгов с указанными критериями
@pytest.mark.asyncio
@pytest.mark.parametrize('criteria, expected', [
    (CRITERIA_REQUEST_1, 0),
    (CRITERIA_REQUEST_2, 2),
    (CRITERIA_REQUEST_3, 4),
    (CRITERIA_REQUEST_4, 1),
    (CRITERIA_REQUEST_5, 2),
])
async def test_getting_results_by_criteria(client, criteria, expected):
    response = await client.post(app.url_path_for('get_trading_results_by_filter'),
                                 json=criteria)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == expected
