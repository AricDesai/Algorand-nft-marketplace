import json
from algosdk import account, mnemonic, algod, transaction
import sys


PURESTAKE_API_KEY = "YOUR_PURESTAKE_API_KEY"
ALGOD_ADDRESS = "https://testnet-algorand.api.purestake.io/ps2"
HEADERS = {
    "X-API-Key": PURESTAKE_API_KEY,
}


algod_client = algod.AlgodClient(PURESTAKE_API_KEY, ALGOD_ADDRESS, headers=HEADERS)

def generate_account():
    private_key, address = account.generate_account()
    print(f"Address: {address}")
    print(f"Mnemonic: {mnemonic.from_private_key(private_key)}")

def get_balance(address):
    try:
        account_info = algod_client.account_info(address)
        balance = account_info.get('amount')
        print(f"Balance for {address}: {balance / 1e6} Algos")
    except Exception as e:
        print(f"Error fetching balance: {str(e)}")

def send_algo(sender_mnemonic, receiver_address, amount):
    try:
        sender_private_key = mnemonic.to_private_key(sender_mnemonic)
        sender_address = account.address_from_private_key(sender_private_key)
        
        params = algod_client.suggested_params()
        
        amount_in_microalgos = int(amount * 1e6)
        
        txn = transaction.PaymentTxn(
            sender=sender_address,
            sp=params,
            receiver=receiver_address,
            amt=amount_in_microalgos,
            note=None
        )
        
        signed_txn = txn.sign(sender_private_key)
        txid = algod_client.send_transaction(signed_txn)
        
        print(f"Transaction sent with txID: {txid}")
        
        wait_for_confirmation(txid)
        
    except Exception as e:
        print(f"Failed to send Algo: {str(e)}")

def wait_for_confirmation(txid):
    last_round = algod_client.status().get('last-round')
    while True:
        try:
            pending_txn = algod_client.pending_transaction_info(txid)
            if pending_txn.get('confirmed-round', 0) > 0:
                print(f"Transaction confirmed in round {pending_txn.get('confirmed-round')}.")
                break
            else:
                print("Waiting for confirmation...")
                last_round += 1
                algod_client.status_after_block(last_round)
        except Exception:
            print("Exception while waiting for confirmation")
            break

def print_help():
    print("""
Usage:
    python algo_wallet_tool.py generate
        # Generate new account and mnemonic

    python algo_wallet_tool.py balance <address>
        # Check balance of an address

    python algo_wallet_tool.py send <sender_mnemonic> <receiver_address> <amount>
        # Send Algos from sender to receiver
""")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "generate":
        generate_account()
    elif command == "balance":
        if len(sys.argv) != 3:
            print("Please provide an address")
            sys.exit(1)
        get_balance(sys.argv[2])
    elif command == "send":
        if len(sys.argv) != 5:
            print("Usage: send <sender_mnemonic> <receiver_address> <amount>")
            sys.exit(1)
        send_algo(sys.argv[2], sys.argv[3], float(sys.argv[4]))
    else:
        print_help()
