from abc import ABC, abstractmethod
from typing import List, Optional
from src.app.entities.transaction import Transaction


class ITransactionRepository(ABC):
    @abstractmethod
    def get_all_transactions(self) -> List[Transaction]:
        """
        Return all stored transactions.

        Returns:
            List[Transaction]: Collection of all transactions currently persisted.
        """
        pass

    @abstractmethod
    def get_transaction(self, transaction_id: str) -> Optional[Transaction]:
        """
        Retrieve a single transaction by its identifier.

        Args:
            transaction_id (str): UUID string stored in the entity attribute `transaction.transaction_id`.

        Returns:
            Optional[Transaction]: The matching transaction when found, otherwise `None`.
        """
        pass

    @abstractmethod
    def create_transaction(self, transaction: Transaction) -> Transaction:
        """
        Persist a new transaction.

        Args:
            transaction (Transaction): Fully validated transaction entity.

        Returns:
            Transaction: The persisted transaction.
        """
        pass

    @abstractmethod
    def delete_transaction(self, transaction_id: str) -> Optional[Transaction]:
        """
        Delete an transaction by its identifier.

        Args:
            transaction_id (str): UUID string of the target transaction.

        Returns:
            Optional[Transaction]: Deleted transaction when found, otherwise `None`.
        """
        pass

    @abstractmethod
    def update_transaction(
        self,
        transaction_id: str = None,
        type: str = None,
        value: float = None,
        current_balance: float = None,
        timestamp: float = None,
    ) -> Optional[Transaction]:
        """
        Update mutable fields of an existing transaction.

        Args:
            transaction_id (str): UUID string of the transaction to update.
            type (str, optional): New type.
            value (float, optional): New value.
            current_balance (float, optional): New current balance.
            timestamp(float, optional): New timestamp.

        Returns:
            Optional[Transaction]: Updated transaction when found, otherwise `None`.
        """
        pass
