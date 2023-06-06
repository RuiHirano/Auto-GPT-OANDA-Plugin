import pandas as pd
from ta.utils import dropna
from ta.momentum import RSIIndicator, StochasticOscillator, TSIIndicator
from ta.trend import SMAIndicator, EMAIndicator, WMAIndicator, MACD, ADXIndicator
from ta.volume import AccDistIndexIndicator

class Indicator:
    def __init__(self):
        pass
    
    def rsi(candlesticks, period):
        if candlesticks:
            df = pd.DataFrame(candlesticks, columns=['close'])
            # Clean NaN values
            df = dropna(df)
            rsi_indicator = RSIIndicator(df['close'], window=float(period))
            current_rsi = rsi_indicator.rsi().iloc[-1]
            return f'Current RSI Value: {current_rsi}'

        if not candlesticks:
            return f'Failed to get candlesticks'
    
    # Simple Moving Average (SMA)
    def sma(self, candlesticks, period: int) -> None:
        if candlesticks:
            df = pd.DataFrame(candlesticks, columns=['close'])
            df = dropna(df)
            sma = SMAIndicator(df['close'], window=float(period))
            return f'Current Simple Moving Average Value: {sma.sma_indicator().iloc()[-1]}'
        else:
            return f'Failed to get candlesticks'
        
    # Exponential Moving Average (EMA)
    def ema(candlesticks, period):
        # Get the candlesticks data
        if candlesticks:
            df = pd.DataFrame(candlesticks, columns=['close'])
            df = dropna(df)
            ema = EMAIndicator(df['close'], window=float(period))
            return f'Current Exponential Moving Average Value: {ema.ema_indicator().iloc()[-1]}'

        if not candlesticks:
            return f'Failed to get candlesticks'
        
    # Weighted Moving Average (WMA)
    def wma(candlesticks, period):
        # Get the candlesticks data
        if candlesticks:
            df = pd.DataFrame(candlesticks, columns=['close'])
            df = dropna(df)
            wma = WMAIndicator(df['close'], window=float(period))
            return f'Current Weighted Moving Average Value: {wma.wma_indicator().iloc()[-1]}'

        if not candlesticks:
            return f'Failed to get candlesticks'
        
    # Moving Average Convergence Divergence (MACD)
    def macd(candlesticks, fast_period, slow_period, signal_period):
        if candlesticks:
            df = pd.DataFrame(candlesticks, columns=['close'])
            # Clean NaN values
            df = dropna(df)
            # Calculate the RSI values
            macd = MACD(df['close'], window_slow=int(
                        12), window_fast=int(26), window_sign=int(9))
            signal_line = macd.macd_signal().iloc()[-1]
            macd_line = macd.macd().iloc()[-1]
            macd_diff = macd.macd_diff().iloc()[-1]
            macd_values = {"macd_line": macd_line, 'macd_diff': macd_diff, 'signal_line': signal_line}
            return f'Current MACD Values: {macd_values}'
        
        if not candlesticks:
            return f'Failed to get candlesticks'
        
    # Average Directional Movement Index (ADX)
    def adx(candlesticks, period):
        if candlesticks:
            df = pd.DataFrame(candlesticks, columns=['high', 'low', 'close'])
            # Clean NaN values
            df = dropna(df)
            # Calculate the RSI values
            adx = ADXIndicator(df['high'], df['low'], df['close'], window=int(period))
            return f' Current Average Directional Movement Index Value: {adx.adx().iloc()[-1]}'

        if not candlesticks:
            return f'Failed to get candlesticks'

    # Accumulation/Distribution Index (ADI)
    def adi(candlesticks):
        if candlesticks:
            df = pd.DataFrame(candlesticks, columns=['high', 'low', 'close', 'tickVolume'])
            # Clean NaN values
            df = dropna(df)
            adi = AccDistIndexIndicator(df['high'], df['low'], df['close'], volume=df['tickVolume'])
            return f'Current Accumulation/Distribution Index: {adi.acc_dist_index().iloc()[-1]}'

        if not candlesticks:
            return f'Failed to get candlesticks'

    def fib_retracements(candlesticks, high, low):
        high = float(high)
        low = float(low)
        levels = [0.236, 0.382, 0.5, 0.618, 0.786]
        diff = high - low
        retracements = []
        for level in levels:
            retracements.append(high - level * diff)
        return f'Current Fibonacci Retracements are: {retracements}'

    # Stochastic Oscillator
    def stochastic_oscillator(candlesticks, period, smooth_period):
        if candlesticks:
            df = pd.DataFrame(candlesticks, columns=['high', 'low', 'close'])
            # Clean NaN values
            df = dropna(df)
            # Calculate the RSI values
            stotch = StochasticOscillator(
                df['high'], df['low'], df['close'], window=int(period), smooth_window=int(smooth_period))
            return f'Current Stochastic Oscillator value is: {stotch.stoch().iloc()[-1]}'

        if not candlesticks:
            return f'Failed to get candlesticks'

    # True Strength Index
    def tsi(candlesticks, slow_period, fast_period):
        if candlesticks:
            df = pd.DataFrame(candlesticks, columns=['close'])
            # Clean NaN values
            df = dropna(df)
            # Calculate the RSI values
            tsi = TSIIndicator(df['close'], window_slow=int(slow_period), window_fast=int(fast_period))
            return f'Current True Strength Index value is: {tsi.tsi().iloc()[-1]}'