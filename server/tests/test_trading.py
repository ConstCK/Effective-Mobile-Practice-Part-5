import pytest

from fastapi import status
from main import app
from tests.constants import PERIOD_REQUEST_1, PERIOD_REQUEST_2, DATES_REQUEST_1, DATES_REQUEST_2, DATES_REQUEST_3, \
    CRITERIA_REQUEST_1, CRITERIA_REQUEST_2, CRITERIA_REQUEST_3, CRITERIA_REQUEST_4, CRITERIA_REQUEST_5


# Тест маршрута для получения последних дат торгов
@pytest.mark.asyncio
@pytest.mark.parametrize('number, expected', [
    (DATES_REQUEST_1, 2),
    (DATES_REQUEST_2, 5),
    (DATES_REQUEST_3, 5),
])
async def test_getting_dates(initial_run, client, number, expected, ):
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


