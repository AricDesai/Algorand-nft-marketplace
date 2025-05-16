from pyteal import compileTeal
from contracts.escrow_sell import approval as sell_approval
from contracts.escrow_buy import approval as buy_approval

with open("artifacts/escrow_sell.teal", "w") as f:
    f.write(compileTeal(sell_approval(), mode=Mode.Signature))

with open("artifacts/escrow_buy.teal", "w") as f:
    f.write(compileTeal(buy_approval(), mode=Mode.Signature))
