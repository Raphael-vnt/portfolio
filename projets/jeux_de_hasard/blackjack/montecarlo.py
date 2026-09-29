import numpy as np

def run_simulation(n_games=1000, soft17=True):
    # Simulation Monte Carlo très simplifiée
    gains = np.random.choice([-1, 1], size=n_games)  # -1 = perte, +1 = gain
    esperance = gains.mean()
    
    return {
        "n_games": n_games,
        "soft17": soft17,
        "esperance": esperance,
        "wins": (gains == 1).sum(),
        "losses": (gains == -1).sum()
    }