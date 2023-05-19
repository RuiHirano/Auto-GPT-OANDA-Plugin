import os
from oandapyV20 import API
from oandapyV20.exceptions import V20Error
import oandapyV20.endpoints.accounts as accounts
from typing import List

OANDA_ACCOUNT_ID = os.getenv("OANDA_ACCOUNT_ID")
OANDA_ACCESS_TOKEN = os.getenv("OANDA_ACCESS_TOKEN")

class Account:
    def __init__(self):
        self.api = API(OANDA_ACCESS_TOKEN)
    
    def get_account_summary(self):
        request = accounts.AccountSummary(OANDA_ACCOUNT_ID)
        response = self.api.request(request)
        return response.json()
    
    def get_account_instruments(self, instruments: str):
        params = {
            "instruments": instruments
        }
        request = accounts.AccountInstruments(OANDA_ACCOUNT_ID, params=params)
        response = self.api.request(request)
        return response.json()