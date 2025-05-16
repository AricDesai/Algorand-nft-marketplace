from algosdk.v2client import algod
from algosdk.future import transaction
from algosdk import account, mnemonic
import json

algod_address = "https://testnet-api.algonode.cloud"
algod_token = ""
client = algod.AlgodClient(algod_token, algod_address)

creator_mnemonic = "your 25-word mnemonic"
creator_private_key = mnemonic.to_private_key(creator_mnemonic)
creator_address = account.address_from_private_key(creator_private_key)

params = client.suggested_params()

txn = transaction.AssetConfigTxn(
    sender=creator_address,
    sp=params,
    total=1,
    default_frozen=False,
    unit_name="NFT",
    asset_name="MyNFT",
    manager=creator_address,
    reserve=None,
    freeze=None,
    clawback=None,
    url="https://example.com/nft-meta.json",
    decimals=0
)

signed_txn = txn.sign(creator_private_key)
txid = client.send_transaction(signed_txn)
transaction.wait_for_confirmation(client, txid)

asset_id = client.pending_transaction_info(txid)["asset-index"]
print("Asset ID:", asset_id)
