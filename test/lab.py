
from auto_gpt_oanda_plugin import Lab

def test_autochartist():
    lab = Lab()
    result = lab.autochartist(instrument="EUR_USD")
    print("result: ", result)
    
def test_calendar():
    lab = Lab()
    result = lab.calendar(instrument="EUR_USD", period=86400000)
    print("result: ", result)
    
def test_commitments_of_traders():
    lab = Lab()
    result = lab.commitments_of_traders(instrument="EUR_USD")
    print("result: ", result)
    
# TODO: Error: The v1 orderbook_data endpoint has been disabled
def test_historical_position_ratios():
    lab = Lab()
    result = lab.historical_position_ratios(instrument="EUR_USD", period=864000)
    print("result: ", result)
    
# TODO: Error: The v1 orderbook_data endpoint has been disabled
def test_orderbook_data():
    lab = Lab()
    result = lab.orderbook_data(instrument="EUR_USD", period=864000)
    print("result: ", result)
    
def test_spreads():
    lab = Lab()
    result = lab.spreads(instrument="EUR_USD", period=30000000)
    print("result: ", result)
    
if __name__ == '__main__':
    # pip install -e .
    # ex: OANDA_ACCESS_TOKEN=xxxxxx OANDA_ACCOUNT_ID='xxx-xxx-xxxxxx-xxx' OANDA_ENVIRONMENT=practice python3 test/lab.py
    test_orderbook_data()
    print("Done!")