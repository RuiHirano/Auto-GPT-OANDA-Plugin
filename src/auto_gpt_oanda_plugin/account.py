import os
from oandapyV20 import API
from oandapyV20.exceptions import V20Error
import oandapyV20.endpoints.accounts as accounts
from .settings import settings

class Account:
    def __init__(self):
        self.api = API(settings.OANDA_ACCESS_TOKEN)
    
    def get_account_summary(self):
        request = accounts.AccountSummary(settings.OANDA_ACCOUNT_ID)
        response = self.api.request(request)
        return response.json()
    
    def get_account_instruments(self, instruments: str):
        params = {
            "instruments": instruments
        }
        request = accounts.AccountInstruments(settings.OANDA_ACCOUNT_ID, params=params)
        response = self.api.request(request)
        return response.json()