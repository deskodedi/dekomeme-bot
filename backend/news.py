# news.py
import random

def get_news_impact(token_name):
    """
    Връща:
    - положително число → hype
    - отрицателно число → panic
    - 0 → неутрално
    """

    impact = random.choice([0, 0.05, 0.1, -0.05, -0.1])

    if impact > 0:
        print(f"[NEWS] Positive sentiment for {token_name}: +{impact}")
    elif impact < 0:
        print(f"[NEWS] Negative sentiment for {token_name}: {impact}")
    else:
        print(f"[NEWS] Neutral sentiment for {token_name}")

    return impact
