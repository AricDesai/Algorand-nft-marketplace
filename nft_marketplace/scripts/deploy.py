from algosdk.v2client import algod
from algosdk import logic, account, mnemonic
from algosdk.future import transaction

algod_address = "https://testnet-api.algonode.cloud"
algod_token = ""
client = algod.AlgodClient(algod_token, algod_address)

creator_mnemonic = "your 25-word mnemonic"
creator_private_key = mnemonic.to_private_key(creator_mnemonic)
creator_address = account.address_from_private_key(creator_private_key)

with open("artifacts/escrow_sell.teal", "r") as f:
    escrow_program = f.read()

lsig = logic.LogicSigAccount(escrow_program)
escrow_address = lsig.address()

params = client.suggested_params()
fund_txn = transaction.PaymentTxn(
    sender=creator_address,
    receiver=escrow_address,
    amt=1000000,
    sp=params
)

signed_fund_txn = fund_txn.sign(creator_private_key)
txid = client.send_transaction(signed_fund_txn)
transaction.wait_for_confirmation(client, txid)

print("Escrow Address:", escrow_address)
