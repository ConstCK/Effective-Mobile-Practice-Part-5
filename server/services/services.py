import datetime

from schemas.trading import DatesPeriod, TradingsFilter


class Utils:
    """Класс с различными сервисными методами"""

    @staticmethod
    def set_key_by_date(period: DatesPeriod) -> str:
        # Метод для формирования ключа кэша для указанного периода запроса
        key_start = period.start_date if period.start_date else 'all'
        key_end = period.end_date if period.end_date else 'all'
        return f'{key_start}:{key_end}'

    @staticmethod
    def set_key_by_criteria(criteria: TradingsFilter) -> str:
        # Метод для формирования ключа кэша для указанных критериев фильтрации запроса
        key_start = criteria.oil_id if criteria.oil_id else 'all'
        key_body = criteria.delivery_type_id if criteria.delivery_type_id else 'all'
        key_end = criteria.delivery_basis_id if criteria.delivery_basis_id else 'all'
        return f'{key_start}:{key_body}:{key_end}'

    @staticmethod
    def calculate_expire_time():
        # Метод для определения expire_time кэша (удаления донных из кэша)
        now = datetime.datetime.now()
        time_point = datetime.datetime(now.year, now.month, now.day, 14, 11, 00)
        if now > time_point:
            expire_time = (datetime.timedelta(1) - (now - time_point))
        else:
            expire_time = time_point - now
        return expire_time
