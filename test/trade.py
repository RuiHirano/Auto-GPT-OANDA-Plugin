
from auto_gpt_oanda_plugin import Trade

def test_order_create():
    trade = Trade()
    result = trade.order_create(
        instrument="EUR_USD",
        price=1.080,
        stop_loss=1.081,
        take_profit=None,
        units=-1000,
        type="LIMIT" # "MARKET", "LIMIT", "STOP"
    )
    print("result: ", result)  
    
def test_order_cancel():
    trade = Trade()
    result = trade.order_cancel(
        order_id='17'
    )
    print("result: ", result)  
    
def test_order_list():
    trade = Trade()
    result = trade.order_list()
    print("result: ", result)
    
def test_trade_details():
    trade = Trade()
    result = trade.trade_details(
        trade_id='14'
    )
    print("result: ", result)
    
def test_trade_list():
    trade = Trade()
    result = trade.trades_list(
        instruments="EUR_USD,USD_JPY"
    )
    print("result: ", result)
    
def test_trade_close():
    trade = Trade()
    result = trade.trade_close(
        trade_id='14',
        units="500"
    )
    print("result: ", result)
    
def test_position_close():
    trade = Trade()
    result = trade.position_close(
        instrument="EUR_USD",
        long_units="ALL", # "ALL" or str units
    )
    print("result: ", result)
    
def test_position_list():
    trade = Trade()
    result = trade.position_list()
    print("result: ", result)
    
def test_position_details():
    trade = Trade()
    result = trade.position_details(
        instrument="EUR_USD"
    )
    print("result: ", result)
    
if __name__ == '__main__':
    # pip install -e .
    # ex: OANDA_ACCESS_TOKEN=xxxxxx OANDA_ACCOUNT_ID='xxx-xxx-xxxxxx-xxx' OANDA_ENVIRONMENT=practice python3 test/trade.py
    test_order_create()
    
    print("Done!")