from typing import Annotated

from fastapi import APIRouter, status, Depends, Body

from crud.crud import TradingService
from database.redis import TradingResultRepository
from schemas.trading import DatesOut, DatesRequest

# Маршрут для операций с торговыми данными
router = APIRouter(prefix='/api/v1/trading')


@router.get('/get_dates', description='Get latest trading dates', response_model=list[DatesOut],
            status_code=status.HTTP_200_OK, name='get_latest_trading_dates',
            responses={200: {'description': 'Успешное получение объектов'},
                       }
            )
async def get_latest_dates(service: Annotated[TradingService, Depends()],
                           number: Annotated[DatesRequest, Body()],
                           cache: Annotated[TradingResultRepository, Depends()]):
    result = await service.get_last_trading_dates(number.number)
    print(cache.__dir__())
    return result
