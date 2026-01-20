# dashboard_push.py
from config import CRITICAL_PROFIT_THRESHOLD, CRITICAL_LOSS_THRESHOLD

def push_alert(token, profit):
    """
    Изпраща alert при важна печалба или загуба
    """

    if profit >= CRITICAL_PROFIT_THRESHOLD:
        print(f"[ALERT 🚀] BIG PROFIT on {token}: +{profit} SOL")

    elif profit <= CRITICAL_LOSS_THRESHOLD:
        print(f"[ALERT ⚠️] BIG LOSS on {token}: {profit} SOL")

    else:
        print(f"[INFO] Trade closed on {token}: {profit} SOL")
