import os
from oandapyV20 import API
from oandapyV20.exceptions import V20Error
import oandapyV20.endpoints.pricing as pricing
import oandapyV20.endpoints.instruments as instruments
from pydantic import BaseModel, EmailStr, Field, validator

OANDA_ACCOUNT_ID = os.getenv("OANDA_ACCOUNT_ID")
OANDA_ACCESS_TOKEN = os.getenv("OANDA_ACCESS_TOKEN")

class Market:
    def __init__(self):
        self.api = API(OANDA_ACCESS_TOKEN)
    
    def instruments_candles(self, instrument: str, granularity: str, count: int) -> None:
        params = {
            "granularity" : granularity,
            "count" : count,
        }
        request = instruments.InstrumentsCandles(instrument=instrument, params = params)
        response = self.api.request(request)
        candlesticks = response.json()
        return candlesticks
    