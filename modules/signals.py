def generate_signal(df, sentiment):
    short_ma = df['Close'].rolling(5).mean()
    long_ma = df['Close'].rolling(20).mean()

    if short_ma.iloc[-1] > long_ma.iloc[-1] and sentiment > 0.1:
        return "BUY"
    elif short_ma.iloc[-1] < long_ma.iloc[-1] and sentiment < -0.1:
        return "SELL"
    return "HOLD"