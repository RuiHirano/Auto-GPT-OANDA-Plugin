import oandapyV20.endpoints.instruments as instruments
from oandapyV20 import API

from .settings import settings

class Market:
    def __init__(self):
        self.api = API(
            access_token=settings.OANDA_ACCESS_TOKEN, 
            environment=settings.OANDA_ENVIRONMENT
        )
    
    def instruments_candles(self, instrument: str, granularity: str, count: int) -> None:
        params = {
            "granularity" : granularity,
            "count" : count,
        }
        r = instruments.InstrumentsCandles(instrument=instrument, params = params)
        self.api.request(r)
        return r.response
