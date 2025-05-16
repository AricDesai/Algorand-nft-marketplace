from algosdk import algod, transaction, account, mnemonic
from utils import get_private_key_from_mnemonic, wait_for_confirmation
import config

def create_asa():
    algod_client = algod.AlgodClient(config.ALGOD_TOKEN, config.ALGOD_ADDRESS, headers=config.HEADERS)
    private_key = get_private_key_from_mnemonic(config.MNEMONIC)
    sender = account.address_from_private_key(private_key)

    params = algod_client.suggested_params()

    txn = transaction.AssetConfigTxn(
        sender=sender,
        sp=params,
        total=1000000,                # total tokens
        decimals=0,                   # no decimals
        default_frozen=False,
        unit_name="MYTK",
        asset_name="MyToken",
        manager=sender,
        reserve=sender,
        freeze=sender,
        clawback=sender,
        url="https://mytoken.example.com",
        metadata_hash=b"16bytesmetadata"
    )

    signed_txn = txn.sign(private_key)
    txid = algod_client.send_transaction(signed_txn)
    print(f"Transaction sent with txID: {txid}")

    confirmed_txn = wait_for_confirmation(algod_client, txid)

    print("ASA ID:", confirmed_txn["asset-index"])

if __name__ == "__main__":
    create_asa()
