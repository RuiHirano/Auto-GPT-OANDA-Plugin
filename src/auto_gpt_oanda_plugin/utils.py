import re

def validate_instrument(instrument: str) -> str:
    patterns = [
        {
            "pattern": '^[A-Z]{3}_[A-Z]{3}$',
            "replace_func": lambda x: x 
        },
        {
            "pattern": '^[A-Z]{3}/[A-Z]{3}$',
            "replace_func": lambda x: x.replace("/", "_")
        }, 
        { 
            "pattern": '^[A-Z]{6}$',
            "replace_func": lambda x: x[:3] + "_" + x[3:]
        },
        {
            "pattern": '^[a-z]{3}_[a-z]{3}$',
            "replace_func": lambda x: x.upper()
        },
        {
            "pattern": '^[a-z]{3}/[a-z]{3}$',
            "replace_func": lambda x: x.upper().replace("/", "_")
        }, 
        { 
            "pattern": '^[a-z]{6}$',
            "replace_func": lambda x: x[:3].upper() + "_" + x[3:].upper()
        },
        ]
    for pattern in patterns:
        if re.match(pattern["pattern"], instrument):
            return pattern["replace_func"](instrument)
    raise ValueError("Invalid instrument: " + instrument)

def validate_granularity(granularity: str) -> str:
    timeframe_map = {
        "1 minute": "M1",
        "1 min": "M1",
        "1min": "M1",
        "1m": "M1",
        "1M": "M1",
        "M1": "M1",
        "5 minutes": "M5",
        "5 min": "M5",
        "5min": "M5",
        "5m": "M5",
        "5M": "M5",
        "M5": "M5",
        "15 minutes": "M15",
        "15 min": "M15",
        "15min": "M15",
        "15m": "M15",
        "15M": "M15",
        "M15": "M15",
        "30 minutes": "M30",
        "30 min": "M30",
        "30min": "M30",
        "30m": "M30",
        "30M": "M30",
        "M30": "M30",
        "1 hour": "H1",
        "1hour": "H1",
        "1hr": "H1",
        "1h": "H1",
        "1H": "H1",
        "H1": "H1",
        "4 hours": "H4",
        "4hours": "H4",
        "4 hrs": "H4",
        "4h": "H4",
        "4H": "H4",
        "H4": "H4",
        "1 day": "D",
        "1day": "D",
        "1d": "D",
        "1D": "D",
        "D1": "D",
        "1 week": "W",
        "1week": "W",
        "1w": "W",
        "1W": "W",
        "W1": "W",
        "1 month": "M",
        "1month": "M",
        "m": "M",
        "M": "M",
        "MN": "M",
        "mn": "M",
    }
    if granularity in timeframe_map:
        return timeframe_map[granularity]
    raise ValueError("Invalid granularity: " + granularity)
