from config import PRICE_THRESHOLD

def check_alert(current_price):
    if current_price >= PRICE_THRESHOLD:
        return f"Alert: Price reached {current_price}"
    return f"Price is {current_price}, below threshold"
