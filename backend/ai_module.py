# ai_module.py
import random

def evaluate_token(token_name):
    """
    Връща:
    - score (0.0 – 1.0): колко е добър токенът
    - adaptive_percent: % от баланса за сделка
    """

    # Demo AI логика (по-късно ще стане реална)
    score = round(random.uniform(0.3, 0.95), 2)

    if score > 0.85:
        adaptive_percent = 40
    elif score > 0.70:
        adaptive_percent = 30
    elif score > 0.55:
        adaptive_percent = 20
    else:
        adaptive_percent = 10

    print(f"[AI] {token_name} | score={score} | trade%={adaptive_percent}")

    return score, adaptive_percent
