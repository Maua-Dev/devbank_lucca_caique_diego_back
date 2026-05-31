from fastapi import HTTPException
import pytest
from src.app.main import deposit_transaction

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
