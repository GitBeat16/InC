import yfinance as yf
import pandas as pd

def load_stock_data(ticker, period="6mo"):
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)
    df.dropna(inplace=True)
    return df