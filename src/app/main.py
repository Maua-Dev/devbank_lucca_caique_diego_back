from datetime import datetime
from fastapi import FastAPI, HTTPException

from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.environments import Environments

from uuid import uuid4


app = FastAPI()

member_repo= Environments.get_member_repo()
transaction_repo= Environments.get_transaction_repo()()



@app.post("/deposit", status_code=201)
def deposit_transaction(request: dict):
    validation_request = Transaction.validate_request(request=request)
    if not validation_request[0]:
        raise HTTPException(
            status_code=400,
            detail=validation_request[1]
        )
    options = ["2", "5", "10", "20", "50", "100", "200"]
    total_value = 0
    for i in options:
        if request.get(i, 0) is None:
            raise HTTPException(
                status_code=400,
                detail="Valor inválido"
            )
        value = float(i) * request.get(i, 0)
        total_value += value
    validation_value = Transaction.validate_value(
        value=float(total_value)
    )
    if not validation_value[0]:
        raise HTTPException(
            status_code=400,
            detail=validation_value[1]
        )
    member = member_repo.get_member(
    "b11af449-22c7-43db-b0e4-dbfbbe7fdbd7"
)
    if member is None:
        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )
    member_current_balance = member.current_balance
    if total_value > (2 * member_current_balance):
        raise HTTPException(
            status_code=403,
            detail="Depósito suspeito"
        )
    member_current_balance += total_value
    deposit_transaction = Transaction(
    transaction_id=str(uuid4()),
    type_value=TransactionTypeEnum.DEPOSIT,
    value=total_value,
    current_balance=member_current_balance,
    timestamp=int(datetime.now().timestamp()),
)
    transaction_repo.create_transaction(
        transaction=deposit_transaction
)
    member_repo.update_member(
        member_id=member.member_id,
        current_balance=member_current_balance
    )
    current_balance = member_current_balance
    return {
        "current balance": current_balance,
        "timestamp": deposit_transaction.timestamp,
    }