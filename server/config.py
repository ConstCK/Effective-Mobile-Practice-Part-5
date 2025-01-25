from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Базовые настройки приложения
    """

    DB_NAME: str
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASSWORD: str
    REDIS: str

    host: str = 'localhost'

    @property
    def db_url(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:5432/{self.DB_NAME}'

    # @property
    # def test_db_url(self):
    #     return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:5432/{self.TEST_DB_NAME}'

    @property
    def redis_url(self):
        return f'redis://{self.REDIS}:6379/0'

    # Настройки для использования переменных из ..env
    model_config = SettingsConfigDict(
        env_file='../.env', env_file_encoding='utf-8', extra='allow')


settings = Settings()
