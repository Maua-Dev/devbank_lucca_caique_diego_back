from fastapi import HTTPException
import pytest
from src.app.main import deposit_transaction, withdraw_transaction
from fastapi.testclient import TestClient
from src.app.main import app
from src.app.repo.transaction_repository_mock import TransactionRepositoryMock

from src.app.main import transaction_repo



@pytest.fixture(autouse=True)
def reset_transaction_repo():

    fresh_repo = TransactionRepositoryMock()

    transaction_repo.transactions = fresh_repo.transactions.copy()


class Test_Main:    
    def test_deposit_transaction(self):
        body = {
            '2': 0,
            '5': 2,
            '10': 0,
            '20': 0,
            '50': 0,
            '100': 0,
            '200': 0
        }

        response= deposit_transaction(request=body)

        assert response == {
            "current balance": 1210.0,
            "timestamp": response.get("timestamp")
        }

    def test_deposit_transaction_value_is_none(self):

        with pytest.raises(HTTPException) as err:
            deposit_transaction(request=None)

    def test_deposit_transaction_value_is_not_dict(self):

        with pytest.raises(HTTPException) as err:
            deposit_transaction(request=1)

    def test_deposit_transaction_request_have_none_arg(self):

        body = {
            '2': 0,
            '5': None,
            '10': 0,
            '20': 0,
            '50': 0,
            '100': 0,
            '200': 0,
        }
        
        with pytest.raises(HTTPException) as err:
            deposit_transaction(request=body)

    def test_deposit_transaction_value_is_negative(self):

        body = {
            '2': 0,
            '5': -2,
            '10': 0,
            '20': 0,
            '50': 0,
            '100': 0,
            '200': 0,
        }

        with pytest.raises(HTTPException) as err:
            deposit_transaction(request=body)

    def test_deposit_transaction_value_to_higher(self):

        body = {
            '2': 0,
            '5': 0,
            '10': 0,
            '20': 0,
            '50': 0,
            '100': 0,
            '200': 13
        }

        with pytest.raises(HTTPException) as err:
            deposit_transaction(request=body)

client = TestClient(app)

class TestWithdraw:

    def test_withdraw_transaction(self):

        body = {
            '2': 0,
            '5': 0,
            '10': 0,
            '20': 0,
            '50': 0,
            '100': 0,
            '200': 1
        }

        response = withdraw_transaction(request=body)

        assert response == {
            "current_balance": 1010.0,
            "timestamp": response.get("timestamp")
        }

    def test_withdraw_transaction_value_is_none(self):

        with pytest.raises(HTTPException):
            withdraw_transaction(request=None)

    def test_withdraw_transaction_value_is_not_dict(self):

        with pytest.raises(HTTPException):
            withdraw_transaction(request=1)

    def test_withdraw_transaction_request_have_none_arg(self):

        body = {
            '2': 0,
            '5': None,
            '10': 0,
            '20': 0,
            '50': 0,
            '100': 0,
            '200': 0,
        }

        with pytest.raises(HTTPException):
            withdraw_transaction(request=body)

    def test_withdraw_transaction_value_is_negative(self):

        body = {
            '2': 0,
            '5': -2,
            '10': 0,
            '20': 0,
            '50': 0,
            '100': 0,
            '200': 0,
        }

        with pytest.raises(HTTPException):
            withdraw_transaction(request=body)

    def test_withdraw_transaction_value_to_higher(self):

        body = {
            '2': 0,
            '5': 0,
            '10': 0,
            '20': 0,
            '50': 0,
            '100': 0,
            '200': 13
        }

        with pytest.raises(HTTPException):
            withdraw_transaction(request=body)

class Test_GetHistory:

    def test_get_history(self):
        repo = TransactionRepositoryMock()

        response = client.get("/transactions/get_history")

        assert response.status_code == 200

        transactions_response = response.json()["all_transactions"]

        assert len(transactions_response) == len(repo.transactions)

        for transaction_response, transaction_mock in zip(
            transactions_response,
            repo.transactions
        ):
            assert transaction_response["transaction_id"] == transaction_mock.transaction_id
            assert transaction_response["type_value"] == transaction_mock.type_value.value
            assert transaction_response["value"] == transaction_mock.value
            assert transaction_response["current_balance"] == transaction_mock.current_balance
            assert transaction_response["timestamp"] == transaction_mock.timestamp