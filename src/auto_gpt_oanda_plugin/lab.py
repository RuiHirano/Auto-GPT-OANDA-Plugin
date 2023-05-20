import os

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
        request = labs.Autochartist(params=params)
        response = self.api.request(request)
        return response.json()
    
    def calendar(self, instrument: str, period: int) -> None:
        params = {
          "instrument": instrument,
          "period": period
        }
        request = labs.Calendar(params=params)
        response = self.api.request(request)
        return response.json()
    
    def commitments_of_traders(self, instrument: str) -> None:
        params = {
          "instrument": instrument,
        }
        request = labs.CommitmentsOfTraders(params=params)
        response = self.api.request(request)
        return response.json()
    
    def historical_position_ratios(self, instrument: str, period: int) -> None:
        params = {
          "instrument": instrument,
          "period": period
        }
        request = labs.HistoricalPositionRatios(params=params)
        response = self.api.request(request)
        return response.json()
    
    def orderbook_data(self, instrument: str, period: int) -> None:
        params = {
          "instrument": instrument,
          "period": period
        }
        request = labs.OrderbookData(params=params)
        response = self.api.request(request)
        return response.json()
    
    def spreads(self, instrument: str, period: int) -> None:
        params = {
          "instrument": instrument,
          "period": period
        }
        request = labs.Spreads(params=params)
        response = self.api.request(request)
        return response.json()
    