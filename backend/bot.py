# bot.py
import time
from datetime import datetime, timedelta
from config import PERCENT_PER_TRADE, HOLD_HOURS
from ai_module import evaluate_token
from history import save_trade
from dashboard_push import push_alert
from news import get_news_impact

BALANCE_SOL = 10.0  # demo balance
OPEN_TRADES = []

TOKENS = ["TOKEN_A", "TOKEN_B", "TOKEN_C"]

def buy_token(token, amount):
    print(f"Buying {token} for {amount} SOL")
    return {"token": token, "amount": amount, "buy_time": datetime.utcnow()}

def sell_token(trade):
    profit = trade["amount"] * 0.15
    print(f"Selling {trade['token']} with profit {profit} SOL")
    return profit

def trading_cycle():
    global BALANCE_SOL

    for token in TOKENS:
        score, adaptive_percent = evaluate_token(token)
        news_impact = get_news_impact(token)

        if score + news_impact > 0.7:
            trade_amount = BALANCE_SOL * (adaptive_percent / 100)
            trade = buy_token(token, trade_amount)
            OPEN_TRADES.append(trade)
            BALANCE_SOL -= trade_amount

    for trade in OPEN_TRADES[:]:
        if datetime.utcnow() - trade["buy_time"] >= timedelta(hours=HOLD_HOURS):
            profit = sell_token(trade)
            BALANCE_SOL += trade["amount"] + profit
            save_trade(trade, profit)
            push_alert(trade["token"], profit)
            OPEN_TRADES.remove(trade)

if __name__ == "__main__":
    while True:
        trading_cycle()
        time.sleep(60)
