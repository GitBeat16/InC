import streamlit as st
import plotly.graph_objects as go
import os
import time

from modules.data_loader import load_stock_data
from modules.sentiment import get_news_sentiment
from modules.monte_carlo import monte_carlo_simulation
from modules.signals import generate_signal

# Load CSS safely
css_path = os.path.join(os.path.dirname(__file__), "ui", "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown('<div class="title">🚀 StockZ Paper Trading Terminal</div>', unsafe_allow_html=True)

ticker = st.text_input("Enter Stock Ticker", "AAPL")

if st.button("Analyze"):

    with st.spinner("Fetching market data..."):
        time.sleep(1)
        df = load_stock_data(ticker)

    if df is None or df.empty:
        st.error("⚠️ Failed to fetch data (Rate limit or invalid ticker). Try again later.")
        st.stop()

    # Price Chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], name='Price'))
    st.plotly_chart(fig)

    # Sentiment
    sentiment_score, headlines = get_news_sentiment(ticker)

    st.subheader("📰 News Sentiment")
    st.write(f"Score: {sentiment_score:.2f}")

    if sentiment_score > 0.1:
        st.success("📈 Positive Sentiment")
    elif sentiment_score < -0.1:
        st.error("📉 Negative Sentiment")
    else:
        st.warning("⚖️ Neutral Sentiment")

    for h in headlines[:5]:
        st.write("-", h)

    # Monte Carlo
    simulations = monte_carlo_simulation(df)

    st.subheader("📊 Monte Carlo Simulation")

    fig_mc = go.Figure()
    for sim in simulations:
        fig_mc.add_trace(go.Scatter(y=sim, mode='lines'))

    st.plotly_chart(fig_mc)

    # Signal
    signal = generate_signal(df, sentiment_score)

    st.subheader("💡 Trading Signal")

    if signal == "BUY":
        st.markdown('<div class="signal-buy">BUY</div>', unsafe_allow_html=True)
    elif signal == "SELL":
        st.markdown('<div class="signal-sell">SELL</div>', unsafe_allow_html=True)
    else:
        st.write("HOLD")
