import datetime
from typing import Annotated

from fastapi import Depends
from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from database.db import get_db
from schemas.trading import DatesRequest, DatesOut
from models.trading import TradingResult as TradingResultModel


class TradingService:
    """
    Класс для операций с данными торговой биржи
    """

    def __init__(self, session: Annotated[AsyncSession,  Depends(get_db)]) -> None:
        self.session = session

    async def get_last_trading_dates(self, dates_number: int) -> list[DatesOut]:
        if not dates_number:
            query = select(TradingResultModel.date)
        else:
            query = (select(TradingResultModel.date)
                     .order_by(desc(TradingResultModel.date))
                     .distinct()
                     .limit(dates_number))
        result = await self.session.execute(query)
        return result.all()


