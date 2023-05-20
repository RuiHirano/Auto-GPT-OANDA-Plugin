from pydantic import BaseSettings

class Settings(BaseSettings):
    OANDA_ACCOUNT_ID: str
    OANDA_ACCESS_TOKEN: str

    # case_sensitive=Trueの場合、環境変数名はフィールド名と一致する必要がある
    class Config:
        case_sensitive = True

settings = Settings()