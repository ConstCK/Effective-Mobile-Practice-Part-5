import datetime

from pydantic import BaseModel, Field, ConfigDict


class BaseTrading(BaseModel):
    oil_id: str | None = Field(description='ID нефти', examples=['A100', ], default=None)
    delivery_type_id: str | None = Field(description='ID типа доставки',
                                         examples=['F', ], default=None)
    delivery_basis_id: str | None = Field(description='ID базиса доставки',
                                          examples=['ANK', ], default=None)


class DatesPeriod(BaseModel):
    start_date: datetime.date = Field(description='Стартовая дата торгов',
                                      examples=['2025-01-10', ], default=None)
    end_date: datetime.date | None = Field(description='Завершающая дата торгов',
                                           examples=['2025-01-10', ], default=None)


class TradingsFilter(BaseTrading):
    pass


class DatesRequest(BaseModel):
    number: int = Field(description='Количество последних дат торгов', gt=0, default=None)


class DatesOut(BaseModel):
    date: datetime.date = Field(description='Даты последних дат торгов')


class TradingsOut(BaseTrading):
    id: int = Field(description='ID результата торгов')

    model_config = ConfigDict(from_attributes=True)

# class TradingsAllOut(BaseTrading):
#     id: int = Field(description='ID результата торгов')
#     exchange_product_id: str = Field(description='Код инструмента')
#     exchange_product_name: str = Field(description='Наименование инструмента')
#     delivery_basis_name: str = Field(description='Базис поставки')
#     volume: int = Field(gt=0, description='Объем договоров в единицах измерения')
#     total: decimal.Decimal = Field(gt=0, description='Объем договоров в руб')
#     count: int = Field(gt=0, description='Количество договоров в руб')
#     date: datetime.date = Field(description='Дата сделки')
#     created_on: datetime.datetime = Field(description='Дата создания записи в БД')
#     updated_on: datetime.datetime = Field(description='Дата обновления записи в БД')
#
#     model_config = ConfigDict(from_attributes=True)
