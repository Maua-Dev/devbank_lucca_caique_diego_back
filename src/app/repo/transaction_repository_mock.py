from typing import Optional, List
from ..entities.transaction import Transaction
from ..enums.transaction_type_enum import TransactionTypeEnum
from .transaction_repository_interface import ITransactionRepository


class TransactionRepositoryMock(ITransactionRepository):
    transactions: List[Transaction]

    def __init__(self):
        self.transactions = [
            Transaction(
                transaction_id="b11af449-22c7-43db-b0e4-dbfbbe7fdbd7",
                type_value=TransactionTypeEnum.DEPOSIT,
                value=550.0,
                current_balance=1200.0,
                timestamp=2,
            ),
            Transaction(
                transaction_id="b21af449-22c7-43db-b0e4-dbfbbe7fdbd7",
                type_value=TransactionTypeEnum.WITHDRAW,
                value=1000.0,
                current_balance=1200.0,
                timestamp=2,
            ),
        ]

    def get_all_transactions(self) -> List[Transaction]:
        return self.transactions

    def get_transaction(self, transaction_id: str) -> Optional[Transaction]:
        for transaction in self.transactions:
            if transaction.transaction_id == transaction_id:
                return transaction

        return None

    def create_transaction(self, transaction: Transaction) -> Transaction:

        self.transactions.append(transaction)

        return transaction

    def delete_transaction(self, transaction_id: str) -> Transaction:
        for transaction in self.transactions:
            if transaction.transaction_id == transaction_id:
                self.transactions.remove(transaction)
                return transaction
        return None

    def update_transaction(
        self,
        transaction_id: str,
        type_value: TransactionTypeEnum = None,
        value: float = None,
        current_balance: float = None,
        timestamp: int = None,
    ) -> Optional[Transaction]:

        for transaction in self.transactions:
            if transaction.transaction_id == transaction_id:
                if type_value is not None:
                    transaction.type_value = type_value
                if value is not None:
                    transaction.value = value
                if timestamp is not None:
                    transaction.timestamp = timestamp
                if current_balance is not None:
                    transaction.current_balance = current_balance
                return transaction
        return None
