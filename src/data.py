import yfinance as yf

def load_data(ticker='AAPL',start='2020-01-01',end='2023-01-01',auto_adjust=True):
    """
    Load Yahoo Finance historical Open, High, Low, Close, Volume (OHLCV) data
    
    Params:
    - ticker (str): Stock symbol
    - start (str): Start date in YYYY-MM-DD
    - end (str): End date in YYYY-MM-DD
    - auto_adjust (Bool): Prices adjusted for corporate actions such as splits and dividends, reflecting true economic value, default=True

    Returns:
    - pd.DataFrame: Daily historical data
    """

    data = yf.download(ticker,start=start,end=end,auto_adjust=auto_adjust)
    return data

# print(load_data())
