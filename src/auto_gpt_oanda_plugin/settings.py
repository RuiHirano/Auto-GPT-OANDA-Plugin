from pydantic import BaseSettings

class Settings(BaseSettings):
    OANDA_ACCOUNT_ID: str
    OANDA_ACCESS_TOKEN: str
    OANDA_ENVIRONMENT: str
    OANDA_ENABLE_COMMANDS: str

    # case_sensitive=Trueの場合、環境変数名はフィールド名と一致する必要がある
    class Config:
        case_sensitive = True
        
    @property
    def __name__(self):
        return "AutoGPTPluginTemplate"

settings = Settings()