# Приложение для получения данных из БД с сайта торгов с 'https://spimex.com/markets/oil_products/trades/results/'


* Скопируйте проект к себе на ПК при помощи: git clone https://github.com/ConstCK/Effective-Mobile-Practice-Part-5.git
* В терминале создайте виртуальное окружение (например python -m venv venv) и активируйте его (venv\scripts\activate)
* Установите все зависимости при помощи pip install -r requirements.txt
* Создайте файл .env в каталоге проекта и пропишите в нем настройки по примеру .env.example
* Запустите Redis сервер при помощи (redis-server) в консоли Ubuntu
* Запустите приложение из каталога проекта (project/python main.py) для запуска приложения
* Для запуска тестов используйте (python -m pytest -vv -s) в консоли из каталога /server

## Примечания:

* На пк должны быть установлены PostgreSQL и Redis сервер
* Для запросов рекомендуется использовать Postman



Endpoints:

* 127.0.0.1:8000/api/v1/trading/get_dates/ - Для получения указанного количества последних дат
* 127.0.0.1:8000/api/v1/trading/get_result_by_period/ - Для получения данных торгов для указанных дат
* 127.0.0.1:8000/api/v1/trading/get_filtered_result/ - Для получения данных торгов с указанными критериями фильтрации
* 127.0.0.1:8000/redoc/ - Документация по типу Redoc
* 127.0.0.1:8000/docs/ - Документация по типу Swagger

