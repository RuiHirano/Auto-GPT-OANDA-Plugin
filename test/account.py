
from auto_gpt_oanda_plugin import Account

def test_get_account_summary():
    account = Account()
    summary = account.get_account_summary()
    print("summary: ", summary)  
    
def test_get_account_instruments():
    account = Account()
    account_instruments = account.get_account_instruments("EUR_USD,USD_JPY")
    print("account_instruments: ", account_instruments)  
    
if __name__ == '__main__':
    # pip install -e .
    # ex: OANDA_ACCESS_TOKEN=xxxxxx OANDA_ACCOUNT_ID='xxx-xxx-xxxxxx-xxx' OANDA_ENVIRONMENT=practice python3 test/account.py
    print("Test get_account_summary()...")
    test_get_account_summary()
    
    print("Test account_instruments()...")
    test_get_account_instruments()
    
    print("Done!")