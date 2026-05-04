from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    INVENTORY_URL: str
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int

    class Config:
        env_file = ".env"

settings = Settings()