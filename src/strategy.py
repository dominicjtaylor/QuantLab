import pandas as pd

def moving_average_crossover(data, short_window=20, long_window=50):
    """
    Generate buy/sell signals using Moving Average Crossover.
    
    Parameters:
    - data (pd.DataFrame): Must contain 'Close' prices.
    - short_window (int): Window for short moving average.
    - long_window (int): Window for long moving average.
    
    Returns:
    - pd.DataFrame: Original data with two new columns:
                      'signal' (1 for buy, 0 for hold, -1 for sell),
                      'position' (cumulative position).
    """

    df = data.copy()
    df['short_ma'] = df['Close'].rolling(window=short_window).mean()
    df['long_ma'] = df['Close'].rolling(window=long_window).mean()
    
    # Signal: 1 when short MA > long MA, else 0
    df['signal'] = 0
    df.loc[df['short_ma'] > df['long_ma'], 'signal'] = 1
    
    # Generate trading orders (1: buy, -1: sell)
    df['position'] = df['signal'].diff()
    
    return df


