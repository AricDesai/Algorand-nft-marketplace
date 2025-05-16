import requests
from config import ALGOD_INDEXER_URL

class IndexerClient:
    def __init__(self):
        self.base_url = ALGOD_INDEXER_URL

    def get_asset_transactions(self, asset_id, limit=100):
        url = f"{self.base_url}/v2/transactions"
        params = {
            "asset-id": asset_id,
            "limit": limit,
            "tx-type": "axfer"
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json().get("transactions", [])
        return []

    def get_asset_price_history(self, asset_id, limit=10):
        txns = self.get_asset_transactions(asset_id, limit)
        prices = []
        for txn in txns:
            if "asset-transfer-transaction" in txn:
                amt = txn["asset-transfer-transaction"].get("amount", 0)
                fee = txn.get("fee", 0)
                if amt > 0:
                    prices.append(amt)
        prices.reverse()
        return prices
