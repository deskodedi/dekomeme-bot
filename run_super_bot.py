# run_super_bot.py
import threading
import time
import json
import os
from backend import bot_real
from backend import telegram_bot
from backend import config

# Terminal colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

# Smart logging
LOG_FILE = "super_bot_log.json"

def log_trade(trade, profit):
    entry = {
        "token": trade["token"],
        "amount": trade["amount"],
        "buy_time": trade["buy_time"].strftime("%Y-%m-%d %H:%M:%S"),
        "sell_time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "profit_sol": profit
    }
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []
    data.append(entry)
    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=4)

def run_trading_bot():
    print(f"{bcolors.HEADER}🤖 Стартира се SUPER bot_real 24/7{bcolors.ENDC}")
    while True:
        bot_real.trading_cycle()
        # Log всички сделки в history + smart log
        for trade in bot_real.OPEN_TRADES[:]:
            elapsed = time.mktime(time.localtime()) - time.mktime(trade["buy_time"])
            if elapsed >= config.HOLD_HOURS * 3600:
                profit = bot_real.sell_token_real(trade)
                bot_real.BALANCE_SOL += trade["amount"] + profit
                bot_real.history.save_trade(trade, profit)
                bot_real.dashboard_push.push_alert(trade["token"], profit)
                log_trade(trade, profit)  # smart logging
                bot_real.OPEN_TRADES.remove(trade)
        time.sleep(5)  # бърз demo; за реални часове → 60 сек

def run_telegram_bot():
    print(f"{bcolors.OKCYAN}📱 Telegram bot активен (24/7){bcolors.ENDC}")
    telegram_bot.run_telegram_bot()

if __name__ == "__main__":
    # Threads за паралелно изпълнение
    t1 = threading.Thread(target=run_trading_bot)
    t2 = threading.Thread(target=run_telegram_bot)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
