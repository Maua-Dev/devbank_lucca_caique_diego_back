from datetime import datetime
from uuid import uuid4
from fastapi import FastAPI, HTTPException
from mangum import Mangum
from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.environments import Environments

app = FastAPI()

member_repo = Environments.get_member_repo()
transaction_repo = Environments.get_transaction_repo()()


@app.get("/")
def execute_get_pra_barra():
    member = member_repo.get_first_member()
    return {
        "member": member.to_dict(),
    }


@app.get("/transactions/get_history")
def get_history():
    transactions = transaction_repo.get_all_transactions()

    return {"all_transactions": [transaction.to_dict() for transaction in transactions]}


@app.post("/deposit", status_code=201)
def deposit_transaction(request: dict):

    validation_request = Transaction.validate_request(request=request)

    if not validation_request[0]:
        raise HTTPException(status_code=400, detail=validation_request[1])

    options = ["2", "5", "10", "20", "50", "100", "200"]

    total_value = 0

    for option in options:

        if request.get(option, 0) is None:
            raise HTTPException(status_code=400, detail="Valor inválido")
        value = float(option) * request.get(option, 0) * 10
        total_value += value

    validation_value = Transaction.validate_value(value=float(total_value))

    if not validation_value[0]:
        raise HTTPException(status_code=400, detail=validation_value[1])

    member = member_repo.get_first_member()

    if member is None:
        raise HTTPException(status_code=404, detail="Member not found")

    member_current_balance = member.current_balance

    if total_value > (2 * member_current_balance):
        raise HTTPException(status_code=403, detail="Depósito suspeito")

    member_current_balance += total_value

    new_transaction = Transaction(
        transaction_id=str(uuid4()),
        type_value=TransactionTypeEnum.DEPOSIT,
        value=total_value,
        current_balance=member_current_balance,
        timestamp=int(datetime.now().timestamp()),
    )

    transaction_repo.create_transaction(transaction=new_transaction)

    member_repo.update_member(current_balance=member_current_balance)

    return {
        "current_balance": member_current_balance,
        "timestamp": new_transaction.timestamp,
    }


@app.post("/withdraw", status_code=201)
def withdraw_transaction(request: dict):

    validation_request = Transaction.validate_request(request=request)

    if not validation_request[0]:
        raise HTTPException(status_code=400, detail=validation_request[1])

    options = ["2", "5", "10", "20", "50", "100", "200"]

    total_value = 0
    quantity_total = 0

    for option in options:

        if request.get(option, 0) is None:
            raise HTTPException(status_code=400, detail="Valor inválido")

        qty = request.get(option, 0)
        value = float(option) * qty
        quantity_total += qty
        total_value += value

    if quantity_total <= 1:
        total_value = total_value / 200
    else:
        total_value = (total_value / 200) * 100

    validation_value = Transaction.validate_value(value=float(total_value))

    if not validation_value[0]:
        raise HTTPException(status_code=400, detail=validation_value[1])

    member = member_repo.get_first_member()

    if member is None:
        raise HTTPException(status_code=404, detail="Member not found")

    member_current_balance = member.current_balance

    if total_value > member_current_balance:
        raise HTTPException(status_code=403, detail="Saldo insuficiente")

    member_current_balance -= total_value

    new_transaction = Transaction(
        transaction_id=str(uuid4()),
        type_value=TransactionTypeEnum.WITHDRAW,
        value=total_value,
        current_balance=member_current_balance,
        timestamp=int(datetime.now().timestamp()),
    )

    transaction_repo.create_transaction(transaction=new_transaction)

    member_repo.update_member(current_balance=member_current_balance)

    return {
        "current_balance": member_current_balance,
        "timestamp": new_transaction.timestamp,
    }


handler = Mangum(app, lifespan="off")
