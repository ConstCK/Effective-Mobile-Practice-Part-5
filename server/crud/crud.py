from typing import Annotated

from fastapi import Depends
from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from database.db import get_db
from schemas.trading import (DatesOut, DatesPeriod,
                             TradingsFilter, TradingsOut, )
from models.trading import TradingResult as TradingResultModel


class TradingService:
    """
    Класс для операций с данными торговой биржи
    """

    def __init__(self, session: Annotated[AsyncSession, Depends(get_db)]) -> None:
        self.session = session

    async def get_last_trading_dates(self, dates_number: int) -> list[DatesOut]:
        # Метод для получения указанного количества списка последних дат торгов
        if not dates_number:
            query = select(TradingResultModel.date)
        else:
            query = (select(TradingResultModel.date)
                     .order_by(desc(TradingResultModel.date))
                     .distinct()
                     .limit(dates_number))
        result = await self.session.execute(query)
        return result.all()

    async def get_tradings_by_period(self, period: DatesPeriod) -> list[TradingsOut]:
        # Метод для получения списка результатов торгов указанного периода
        query = select(TradingResultModel.id,
                       TradingResultModel.oil_id,
                       TradingResultModel.delivery_type_id,
                       TradingResultModel.delivery_basis_id,
                       )
        if period.start_date:
            query = query.where(TradingResultModel.date >= period.start_date)
        if period.end_date:
            query = query.where(TradingResultModel.date <= period.end_date)

        result = await self.session.execute(query)
        return result.all()

    async def get_filtered_tradings(self, criteria: TradingsFilter) -> list[TradingsOut]:
        # Метод для получения списка результатов торгов с указанными критериями
        # фильтрации запроса

        query = select(TradingResultModel.id,
                       TradingResultModel.oil_id,
                       TradingResultModel.delivery_type_id,
                       TradingResultModel.delivery_basis_id,
                       )
        if criteria.oil_id:
            query = query.where(TradingResultModel.oil_id == criteria.oil_id)
        if criteria.delivery_type_id:
            query = query.where(TradingResultModel.delivery_type_id == criteria.delivery_type_id)
        if criteria.delivery_basis_id:
            query = query.where(TradingResultModel.delivery_basis_id == criteria.delivery_basis_id)
        result = await self.session.execute(query)
        return result.all()
