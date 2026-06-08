from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="../.env")
    
    DATABASE_URL: str
    REDIS_URL: str
    RABBITMQ_URL: str
    RABBITMQ_USER: str
    RABBITMQ_PASS: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    LANGFUSE_SECRET_KEY: str
    LANGFUSE_PUBLIC_KEY: str
    LANGFUSE_HOST: str
    SECRET_KEY: str
    MODEL_PATH: str

settings = Settings()