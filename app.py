import streamlit as st
import plotly.graph_objects as go
import os

from modules.data_loader import load_stock_data
from modules.sentiment import get_news_sentiment
from modules.monte_carlo import monte_carlo_simulation
from modules.signals import generate_signal

# Load CSS
css_path = os.path.join(os.path.dirname(__file__), "ui", "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown('<div class="title">🚀 StockZ Terminal</div>', unsafe_allow_html=True)

ticker = st.text_input("Enter Ticker", "AAPL")

if st.button("Analyze"):

    df = load_stock_data(ticker)

    if df.empty:
        st.error("Invalid ticker")
        st.stop()

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Close']))
    st.plotly_chart(fig)

    sentiment, headlines = get_news_sentiment(ticker)

    st.subheader("📰 News")
    for h in headlines[:5]:
        st.write("-", h)

    sims = monte_carlo_simulation(df)

    fig2 = go.Figure()
    for s in sims:
        fig2.add_trace(go.Scatter(y=s))
    st.plotly_chart(fig2)

    signal = generate_signal(df, sentiment)

    st.subheader("Signal")

    if signal == "BUY":
        st.markdown('<div class="signal-buy">BUY</div>', unsafe_allow_html=True)
    elif signal == "SELL":
        st.markdown('<div class="signal-sell">SELL</div>', unsafe_allow_html=True)
    else:
        st.write("HOLD")