import os
from oandapyV20 import API
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.trades as trades
import oandapyV20.endpoints.positions as positions
from typing import Optional, Union
from .settings import settings

class Trade:
    def __init__(self):
        self.api = API(settings.OANDA_ACCESS_TOKEN)
    
    def order_create(self, instrument: str, price: float, units: int, stop_loss: Optional[float]=None, take_profit: Optional[float]=None, type: str="MARKET") -> None:
        data = {
            "order": {
                "price": str(price),
                "instrument": instrument,
                "units": str(units),
                "type": type,
                "positionFill": "DEFAULT"
            }
        }
        if stop_loss:
            data["order"]["stopLossOnFill"] = {
                "price": str(stop_loss)
            }
        if take_profit:
            data["order"]["takeProfitOnFill"] = {
                "price": str(take_profit)
            }
        r = orders.OrderCreate(settings.OANDA_ACCOUNT_ID, data=data)
        self.api.request(r)
        return r.response
    
    def order_cancel(self, order_id: str) -> None:
        r = orders.OrderCancel(settings.OANDA_ACCOUNT_ID, orderID=order_id)
        self.api.request(r)
        return r.response
    
    def order_details(self, order_id: str) -> None:
        r = orders.OrderDetails(settings.OANDA_ACCOUNT_ID, orderID=order_id)
        self.api.request(r)
        return r.response
    
    def order_list(self) -> None:
        r = orders.OrderList(settings.OANDA_ACCOUNT_ID)
        self.api.request(r)
        return r.response
    
    def trade_close(self, trade_id: str, units: str) -> None:
        data = {
            "units": units
        }
        r = trades.TradeClose(settings.OANDA_ACCOUNT_ID, tradeID=trade_id, data=data)
        self.api.request(r)
        return r.response
    
    def trade_details(self, trade_id: str) -> None:
        r = trades.TradeDetails(settings.OANDA_ACCOUNT_ID, tradeID=trade_id)
        self.api.request(r)
        return r.response
    
    def trades_list(self, instruments: str) -> None:
        params = {
            "instruments": instruments
        }
        r = trades.TradesList(settings.OANDA_ACCOUNT_ID, params=params)
        self.api.request(r)
        return r.response
    
    def position_close(self, instrument: str, long_units: Optional[Union[int,str]] = None, short_units: Optional[Union[int,str]] = None) -> None:
        data = {}
        if long_units:
            data["longUnits"] = str(long_units)
        elif short_units:
            data["shortUnits"] = str(short_units)
            
        r = positions.PositionClose(settings.OANDA_ACCOUNT_ID, instrument=instrument, data=data)
        self.api.request(r)
        return r.response
    
    def position_details(self, instrument: str) -> None:
        r = positions.PositionDetails(accountID=settings.OANDA_ACCOUNT_ID, instrument=instrument)
        self.api.request(r)
        return r.response
        
    def position_list(self) -> None:
        r = positions.PositionList(settings.OANDA_ACCOUNT_ID)
        self.api.request(r)
        return r.response
        