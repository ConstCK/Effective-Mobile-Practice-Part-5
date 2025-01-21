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
