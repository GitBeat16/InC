import yfinance as yf
import streamlit as st

@st.cache_data(ttl=600)
def load_stock_data(ticker, period="6mo"):
    try:
        df = yf.download(ticker, period=period, progress=False)

        if df is None or df.empty:
            return None

        df.dropna(inplace=True)
        return df

    except Exception as e:
        return None
