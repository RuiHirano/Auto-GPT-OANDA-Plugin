import oandapyV20.endpoints.forexlabs as labs
from oandapyV20 import API

from .settings import settings


class Lab:
    def __init__(self):
        self.api = API(settings.OANDA_ACCESS_TOKEN)
        
    def autochartist(self, instrument: str) -> None:
        params = {
          "instrument": instrument
        }
        r = labs.Autochartist(params=params)
        self.api.request(r)
        return r.response
    
    def calendar(self, instrument: str, period: int) -> None:
        params = {
          "instrument": instrument,
          "period": period
        }
        r = labs.Calendar(params=params)
        self.api.request(r)
        return r.response
    
    def commitments_of_traders(self, instrument: str) -> None:
        params = {
          "instrument": instrument,
        }
        r = labs.CommitmentsOfTraders(params=params)
        self.api.request(r)
        return r.response
    
    # TODO: Deprecated: The v1 orderbook_data endpoint has been disabled. It is library probrem.
    def historical_position_ratios(self, instrument: str, period: int) -> None:
        params = {
          "instrument": instrument,
          "period": period
        }
        r = labs.HistoricalPositionRatios(params=params)
        self.api.request(r)
        return r.response
    
    # TODO: Deprecated: The v1 orderbook_data endpoint has been disabled. It is library probrem.
    def orderbook_data(self, instrument: str, period: int) -> None:
        params = {
          "instrument": instrument,
          "period": period
        }
        r = labs.OrderbookData(params=params)
        self.api.request(r)
        return r.response
    
    def spreads(self, instrument: str, period: int) -> None:
        params = {
          "instrument": instrument,
          "period": period
        }
        r = labs.Spreads(params=params)
        self.api.request(r)
        return r.response
    