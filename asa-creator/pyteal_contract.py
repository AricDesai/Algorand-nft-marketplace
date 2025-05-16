from pyteal import *

def approval_program():
   
    program = Seq([
        Return(Int(1))
    ])
    return program

def clear_state_program():
    return Return(Int(1))

if __name__ == "__main__":
    with open("approval.teal", "w") as f:
        compiled = compileTeal(approval_program(), Mode.Application, version=2)
        f.write(compiled)
    
    with open("clear_state.teal", "w") as f:
        compiled = compileTeal(clear_state_program(), Mode.Application, version=2)
        f.write(compiled)
