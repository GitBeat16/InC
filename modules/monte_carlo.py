import numpy as np

def monte_carlo_simulation(df, num_simulations=10, days=30):
    returns = df['Close'].pct_change().dropna()
    
    mean = returns.mean()
    std_dev = returns.std()

    last_price = df['Close'].iloc[-1]

    simulations = []

    for _ in range(num_simulations):
        prices = [last_price]

        for _ in range(days):
            shock = np.random.normal(mean, std_dev)
            price = prices[-1] * (1 + shock)
            prices.append(price)

        simulations.append(prices)

    return simulations
