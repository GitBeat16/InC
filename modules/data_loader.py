import yfinance as yf

def load_stock_data(ticker, period="6mo"):
    df = yf.Ticker(ticker).history(period=period)
    df.dropna(inplace=True)
    return df