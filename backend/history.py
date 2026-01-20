# history.py
import json
from datetime import datetime

HISTORY_FILE = "trade_history.json"

def save_trade(trade, profit):
    """
    Записва сделка във файл:
    - токен
    - сума
    - време на покупка
    - печалба
    """

    record = {
        "token": trade["token"],
        "amount": trade["amount"],
        "buy_time": trade["buy_time"].isoformat(),
        "sell_time": datetime.utcnow().isoformat(),
        "profit_sol": round(profit, 4)
    }

    try:
        with open(HISTORY_FILE, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(record)

    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

    print(f"[HISTORY] Trade saved: {record}")
