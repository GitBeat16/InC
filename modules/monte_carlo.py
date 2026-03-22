import numpy as np

def monte_carlo_simulation(df, sims=10, days=30):
    returns = df['Close'].pct_change().dropna()
    mean = returns.mean()
    std = returns.std()

    last_price = df['Close'].iloc[-1]

    simulations = []

    for _ in range(sims):
        prices = [last_price]
        for _ in range(days):
            shock = np.random.normal(mean, std)
            prices.append(prices[-1]*(1+shock))
        simulations.append(prices)

    return simulations