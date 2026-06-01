import src.app.main as main_module
from src.app.main import app, execute_get_pra_barra, deposit_transaction, withdraw_transaction, transaction_repo
from src.app.repo.member_repository_mock import MemberRepositoryMock
from src.app.repo.transaction_repository_mock import TransactionRepositoryMock
from fastapi import HTTPException
import pytest
from fastapi.testclient import TestClient

class Test_Main:
    FIRST_MEMBER_ID = "b11af449-22c7-43db-b0e4-dbfbbe7fdbd7"

    def setup_method(self):
        main_module.member_repo = MemberRepositoryMock()

    def test_execute_get_pra_barra(self):
        repo = MemberRepositoryMock()
        response = execute_get_pra_barra()
        expected_member = repo.get_first_member()
        assert response == {
            "member_id": self.FIRST_MEMBER_ID,
            "member": expected_member.to_dict(),
        }

@pytest.fixture(autouse=True)
def reset_transaction_repo():

    fresh_repo = TransactionRepositoryMock()

    transaction_repo.transactions = fresh_repo.transactions.copy()


class Test_Main:
    def setup_method(self):
        main_module.member_repo = MemberRepositoryMock()

    def test_execute_get_pra_barra(self):
        repo = MemberRepositoryMock()
        response = execute_get_pra_barra()
        expected_member = repo.get_first_member()
        assert response == {
            "member_id": self.FIRST_MEMBER_ID,
            "member": expected_member.to_dict(),
        }
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
