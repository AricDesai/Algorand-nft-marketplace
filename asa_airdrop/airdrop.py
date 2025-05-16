import csv
import sys
from algosdk import mnemonic
from algosdk.v2client import algod
from algosdk.future.transaction import AssetTransferTxn



ALGOD_ADDRESS = "https://testnet-algorand.api.purestake.io/ps2"
ALGOD_TOKEN = "<Your PureStake API Key>" 
HEADERS = {
    "X-API-Key": ALGOD_TOKEN,
}

SENDER_MNEMONIC = "<Your 25-word mnemonic here>" 
ASA_ID = 12345678 
AMOUNT = 10  

CSV_FILE = "addresses.csv"  



def get_private_key_from_mnemonic(mn):
    return mnemonic.to_private_key(mn)

def send_asa(client, sender_pk, sender_addr, receiver_addr, asset_id, amount):
    params = client.suggested_params()
    txn = AssetTransferTxn(
        sender=sender_addr,
        sp=params,
        receiver=receiver_addr,
        amt=amount,
        index=asset_id
    )
    signed_txn = txn.sign(sender_pk)
    txid = client.send_transaction(signed_txn)
    print(f"Sent {amount} of ASA {asset_id} to {receiver_addr}, txID: {txid}")
    return txid

def main():
    sender_pk = get_private_key_from_mnemonic(SENDER_MNEMONIC)
    sender_addr = mnemonic.to_public_key(SENDER_MNEMONIC)

    client = algod.AlgodClient(ALGOD_TOKEN, ALGOD_ADDRESS, HEADERS)

    try:
        with open(CSV_FILE, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                receiver = row['address'].strip()
                try:
                    send_asa(client, sender_pk, sender_addr, receiver, ASA_ID, AMOUNT)
                except Exception as e:
                    print(f"Failed to send to {receiver}: {e}")
    except FileNotFoundError:
        print(f"CSV file '{CSV_FILE}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
