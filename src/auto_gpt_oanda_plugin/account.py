from oandapyV20 import API
import oandapyV20.endpoints.accounts as accounts
from .settings import settings

class Account:
    def __init__(self):
        self.api = API(settings.OANDA_ACCESS_TOKEN)
    
    def get_account_summary(self):
        r = accounts.AccountSummary(settings.OANDA_ACCOUNT_ID)
        self.api.request(r)
        return r.response
    
    def get_account_instruments(self, instruments: str):
        params = {
            "instruments": instruments
        }
        r = accounts.AccountInstruments(settings.OANDA_ACCOUNT_ID, params=params)
        self.api.request(r)
        return r.response