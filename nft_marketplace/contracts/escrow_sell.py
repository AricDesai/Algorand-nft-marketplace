from pyteal import *

def approval():
    return And(
        Txn.type_enum() == TxnType.AssetTransfer,
        Txn.asset_amount() == Int(1),
        Txn.asset_receiver() == Addr("BUYER_ADDRESS"),
        Txn.asset_sender() == Global.current_application_address()
    )

print(compileTeal(approval(), mode=Mode.Signature))
