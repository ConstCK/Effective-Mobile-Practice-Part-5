import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    """
    Базовые настройки приложения
    """
    db_url: str = (f"postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
                   f"@{os.getenv('DB_HOST')}:5432/{os.getenv('DB_NAME')}")

    host: str = 'localhost'

    redis_url: str = f'redis://{os.getenv('REDIS')}:6379/0'

    # Настройки для использования переменных из .env
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8', extra='allow')


settings = Settings()
