from indexer_client import IndexerClient
from alert import check_alert
from config import ASA_ID

def main():
    client = IndexerClient()
    prices = client.get_asset_price_history(ASA_ID, limit=20)
    if not prices:
        print("No price data found")
        return

    first = prices[0]
    last = prices[-1]
    change_pct = ((last - first) / first) * 100 if first else 0
    print(f"Price changed by {change_pct:.2f}% over last {len(prices)} transactions")
    print(check_alert(last))

if __name__ == "__main__":
    main()
