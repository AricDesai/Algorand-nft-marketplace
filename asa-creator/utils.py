from algosdk import account, mnemonic, transaction, algod

def get_private_key_from_mnemonic(mn):
    return mnemonic.to_private_key(mn)

def wait_for_confirmation(client, txid):
    last_round = client.status().get('last-round')
    while True:
        txinfo = client.pending_transaction_info(txid)
        if txinfo.get('confirmed-round', 0) > 0:
            print(f"Transaction {txid} confirmed in round {txinfo['confirmed-round']}.")
            return txinfo
        last_round += 1
        client.status_after_block(last_round)
