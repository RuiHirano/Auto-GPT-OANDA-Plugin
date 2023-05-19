import os
from oandapyV20 import API
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.trades as trades
import oandapyV20.endpoints.positions as positions
from typing import List, Optional

OANDA_ACCOUNT_ID = os.getenv("OANDA_ACCOUNT_ID")
OANDA_ACCESS_TOKEN = os.getenv("OANDA_ACCESS_TOKEN")

class Trade:
    def __init__(self):
        self.api = API(OANDA_ACCESS_TOKEN)
    
    def order_create(self, instrument: str, price: float, stop_loss: Optional[float], take_profit: Optional[float], units: float, type: str) -> None:
        data = {
            "order": {
                "price": price,
                "timeInForce": "GTC",
                "instrument": instrument,
                "units": units,
                "type": type,
                "positionFill": "DEFAULT"
            }
        }
        if stop_loss:
            data["order"]["stopLossOnFill"] = {
                "timeInForce": "GTC",
                "price": stop_loss
            }
        if take_profit:
            data["order"]["takeProfitOnFill"] = {
                "timeInForce": "GTC",
                "price": take_profit
            }
        r = orders.OrderCreate(OANDA_ACCOUNT_ID, data=data)
        self.api.request(r)
        return r.response
    
    def order_cancel(self, order_id: str) -> None:
        r = orders.OrderCancel(OANDA_ACCOUNT_ID, orderID=order_id)
        self.api.request(r)
        return r.response
    
    def order_details(self, order_id: str) -> None:
        r = orders.OrderDetails(OANDA_ACCOUNT_ID, orderID=order_id)
        self.api.request(r)
        return r.response
    
    def order_list(self) -> None:
        r = orders.OrderList(OANDA_ACCOUNT_ID)
        self.api.request(r)
        return r.response
    
    def trade_close(self, trade_id: str, units: float) -> None:
        data = {
            "units": units
        }
        r = trades.TradeClose(OANDA_ACCOUNT_ID, tradeID=trade_id, data=data)
        self.api.request(r)
        return r.response
    
    def trade_details(self, trade_id: str) -> None:
        r = trades.TradeDetails(OANDA_ACCOUNT_ID, tradeID=trade_id)
        self.api.request(r)
        return r.response
    
    def trades_list(self, instruments: str) -> None:
        params = {
            "instruments": instruments
        }
        r = trades.TradesList(OANDA_ACCOUNT_ID, params=params)
        self.api.request(r)
        return r.response
    
    # not implemented
    def position_close(self, instrument: str) -> None:
        data = {
            "longUnits": "ALL"
        }
        r = positions.PositionClose(OANDA_ACCOUNT_ID, instrument=instrument, data=data)
        self.api.request(r)
        return r.response
    
    # not implemented
    def position_details(self, instrument: str) -> None:
        r = positions.PositionDetails(accountID=OANDA_ACCOUNT_ID, instrument=instrument)
        self.api.request(r)
        return r.response
        
    # not implemented
    def position_list(self) -> None:
        r = positions.PositionList(OANDA_ACCOUNT_ID)
        self.api.request(r)
        return r.response
        