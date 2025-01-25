import datetime

TRADING_RESULT_1 = {
    'id': 1,
    'exchange_product_id': 'A100ANK060F',
    'exchange_product_name': 'Бензин (АИ-100-К5), Ангарск-группа станций (ст. отправления)',
    'oil_id': 'A100',
    'delivery_basis_id': 'ANK',
    'delivery_basis_name': 'Ангарск-группа станций',
    'delivery_type_id': 'F',
    'volume': 60,
    'total': 4974780,
    'count': 1,
    'date': datetime.datetime(2025, 1, 13),
    'created_on': datetime.datetime.now(),
    'updated_on': datetime.datetime.now(),
}

TRADING_RESULT_2 = {
    'id': 2,
    'exchange_product_id': 'A592ALL060J',
    'exchange_product_name': 'Бензин (АИ-92-К5) по ГОСТ, ст. Аллагуват (ст. отправления ОТП)',
    'oil_id': 'A592',
    'delivery_basis_id': 'ALL',
    'delivery_basis_name': 'Ангарск-группа станций',
    'delivery_type_id': 'J',
    'volume': 30,
    'total': 500000,
    'count': 2,
    'date': datetime.datetime(2025, 1, 12),
    'created_on': datetime.datetime.now(),
    'updated_on': datetime.datetime.now(),
}

TRADING_RESULT_3 = {
    'id': 3,
    'exchange_product_id': 'A592AVM005A',
    'exchange_product_name': 'Бензин (АИ-92-К5) по ГОСТ, ст. Аллагуват (ст. отправления ОТП)',
    'oil_id': 'A592',
    'delivery_basis_id': 'ALL',
    'delivery_basis_name': 'Ангарск-группа станций',
    'delivery_type_id': 'A',
    'volume': 50,
    'total': 33333,
    'count': 3,
    'date': datetime.datetime(2025, 1, 11),
    'created_on': datetime.datetime.now(),
    'updated_on': datetime.datetime.now(),
}

TRADING_RESULT_4 = {
    'id': 4,
    'exchange_product_id': 'A692AVM005A',
    'exchange_product_name': 'Бензин (АИ-92-К5) ГОСТ 32513-2013/ГОСТ 32513-2023,'
                             ' СН КНПЗ (самовывоз автотранспортом)',
    'oil_id': 'A592',
    'delivery_basis_id': 'AVM',
    'delivery_basis_name': 'Ангарск-группа станций',
    'delivery_type_id': 'A',
    'volume': 7,
    'total': 10000,
    'count': 4,
    'date': datetime.datetime(2025, 1, 10),
    'created_on': datetime.datetime.now(),
    'updated_on': datetime.datetime.now(),
}

TRADING_RESULT_5 = {
    'id': 5,
    'exchange_product_id': 'A592AVM005A',
    'exchange_product_name': 'Бензин (АИ-92-К5) ГОСТ 32513-2013/ГОСТ 32513-2023,'
                             ' СН КНПЗ (самовывоз автотранспортом)',
    'oil_id': 'A592',
    'delivery_basis_id': 'AVM',
    'delivery_basis_name': 'Ангарск-группа станций',
    'delivery_type_id': 'A',
    'volume': 7,
    'total': 10000,
    'count': 5,
    'date': datetime.datetime(2025, 1, 9),
    'created_on': datetime.datetime.now(),
    'updated_on': datetime.datetime.now(),
}

DATES_REQUEST_1 = {
    "number": 2
}
DATES_REQUEST_2 = {
    "number": 5
}
DATES_REQUEST_3 = {
    "number": 15
}
PERIOD_REQUEST_1 = {
    "start_date": "2025-01-10",
    "end_date": "2025-01-11"
}
PERIOD_REQUEST_2 = {
    "start_date": "2024-01-11",
    "end_date": "2026-01-12"
}

CRITERIA_REQUEST_1 = {
        "oil_id": "A986",
        "delivery_type_id": "A",
        "delivery_basis_id": "AVM"
}
CRITERIA_REQUEST_2 = {
        "oil_id": "A592",
        "delivery_type_id": "A",
        "delivery_basis_id": "AVM"
}
CRITERIA_REQUEST_3 = {
        "oil_id": "A592",
}

CRITERIA_REQUEST_4 = {
        "oil_id": "A592",
        "delivery_type_id": "J",
}

CRITERIA_REQUEST_5 = {
        "delivery_basis_id": "AVM"
}

INITIAL_DATA = [TRADING_RESULT_1,
                TRADING_RESULT_2,
                TRADING_RESULT_3,
                TRADING_RESULT_4,
                TRADING_RESULT_5]
