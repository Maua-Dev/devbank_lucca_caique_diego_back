from src.app.entities.transaction import Transaction
from src.app.repo.transaction_repository_mock import TransactionRepositoryMock


class Test_TransactionRepositoryMock:
    FIRST_TRANSACTION_ID = "b11af449-22c7-43db-b0e4-dbfbbe7fdbd7"
    NOT_FOUND_TRANSACTION_ID = "00000000-0000-0000-0000-000000000000"
    CREATED_TRANSACTION_ID = "88f0920c-0de0-4e0a-bb46-abdb3705579d"

    def test_get_all_transactions(self):
        repo = TransactionRepositoryMock()
        transactions = repo.get_all_transactions()
        assert len(transactions) == len(repo.transactions)
        assert all(
            [
                transaction_expect == transaction
                for transaction_expect, transaction in zip(
                    repo.transactions, transactions
                )
            ]
        )

    def test_get_transaction(self):
        repo = TransactionRepositoryMock()
        transaction = repo.get_transaction(transaction_id=self.FIRST_TRANSACTION_ID)
        assert transaction is not None
        assert transaction.transaction_id == self.FIRST_TRANSACTION_ID

    def test_get_transaction_not_found(self):
        repo = TransactionRepositoryMock()
        transaction = repo.get_transaction(transaction_id=self.NOT_FOUND_TRANSACTION_ID)
        assert transaction is None

    def test_create_transaction(self):
        repo = TransactionRepositoryMock()
        len_before = len(repo.transactions)
        transaction = Transaction(
            transaction_id=self.CREATED_TRANSACTION_ID,
            type_value="Deposit",
            value=500.0,
            current_balance=1000.0,
            timestamp=5.0,
        )
        repo.create_transaction(transaction=transaction)
        len_after = len(repo.transactions)
        assert len_after == len_before + 1
        assert repo.transactions[-1] == transaction
        assert repo.transactions[-1].transaction_id == self.CREATED_TRANSACTION_ID

    def test_delete_transaction(self):
        repo = TransactionRepositoryMock()
        transaction_expected_to_be_deleted = repo.get_transaction(self.FIRST_TRANSACTION_ID)
        len_before = len(repo.transactions)

        transaction = repo.delete_transaction(transaction_id=self.FIRST_TRANSACTION_ID)
        len_after = len(repo.transactions)
        assert len_after == len_before - 1
        assert transaction == transaction_expected_to_be_deleted
        assert repo.get_transaction(self.FIRST_TRANSACTION_ID) is None

    def test_delete_transaction_not_found(self):
        repo = TransactionRepositoryMock()
        transaction = repo.delete_transaction(transaction_id=self.NOT_FOUND_TRANSACTION_ID)
        assert transaction is None

    def test_update_transaction(self):
        repo = TransactionRepositoryMock()
        transaction_updated = repo.update_transaction(
            transaction_id=self.FIRST_TRANSACTION_ID,
            type_value="Deposit",
            value=500.0,
            current_balance=1000.0,
            timestamp=5.0,
        )

        assert transaction_updated is not None
        assert transaction_updated.transaction_id == self.FIRST_TRANSACTION_ID
        assert transaction_updated.type_value == "Deposit"
        assert transaction_updated.value == 500.0
        assert transaction_updated.current_balance == 1000.0
        assert transaction_updated.timestamp == 5.0

    def test_update_transaction_type_value(self):
        repo = TransactionRepositoryMock()
        type_value = "Deposit"
        transaction_updated = repo.update_transaction(
            transaction_id=self.FIRST_TRANSACTION_ID, type_value=type_value
        )

        assert transaction_updated.type_value == type_value
        assert repo.get_transaction(self.FIRST_TRANSACTION_ID).type_value == type_value

    def test_update_transaction_value(self):
        repo = TransactionRepositoryMock()
        value = 500.0
        transaction_updated = repo.update_transaction(
            transaction_id=self.FIRST_TRANSACTION_ID, value=value
        )

        assert transaction_updated.value == value
        assert repo.get_transaction(self.FIRST_TRANSACTION_ID).value == value
