from pyteal import *

def approval():
    return And(
        Txn.type_enum() == TxnType.Payment,
        Txn.amount() >= Int(1000000),
        Txn.receiver() == Addr("SELLER_ADDRESS")
    )

print(compileTeal(approval(), mode=Mode.Signature))
