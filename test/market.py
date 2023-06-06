
from auto_gpt_oanda_plugin import Market

def test_instruments_candles():
    market = Market()
    candles = market.instruments_candles(instrument="EUR_USD", granularity="M1", count=10)
    print("candles: ", candles)
    
if __name__ == '__main__':
    # pip install -e .
    # ex: OANDA_ACCESS_TOKEN=xxxxxx OANDA_ACCOUNT_ID='xxx-xxx-xxxxxx-xxx' OANDA_ENVIRONMENT=practice python3 test/market.py
    test_instruments_candles()
    print("Done!")