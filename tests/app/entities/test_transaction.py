import pytest
from src.app.entities.transaction import Transaction
from src.app.errors.entity_errors import ParamNotValidated
from src.app.enums.transaction_type_enum import TransactionTypeEnum


class Test_Transaction:
    FIXED_ID = "88f0920c-0de0-4e0a-bb46-abdb3705579d"

    def test_transaction(self):
        transaction = Transaction(
            transaction_id=self.FIXED_ID,
            type_value=TransactionTypeEnum.WITHDRAW,
            value=1000.0,
            current_balance=2000.0,
            timestamp=1231313112,
        )
        assert transaction.type_value == TransactionTypeEnum.WITHDRAW
        assert transaction.value == 1000.0
        assert transaction.current_balance == 2000.0
        assert transaction.timestamp == 1231313112

    def test_transaction_id_required(self):
        with pytest.raises(ParamNotValidated):
            Transaction(
                transaction_id=None,
                type_value=TransactionTypeEnum.WITHDRAW,
                value=1000.0,
                current_balance=2000.0,
                timestamp=1231313112,
            )

    def test_transaction_id_not_string(self):
        with pytest.raises(ParamNotValidated):
            Transaction(
                transaction_id=123141231231,
                type_value=TransactionTypeEnum.WITHDRAW,
                value=1000.0,
                current_balance=2000.0,
                timestamp=1231313112,
            )

    def test_transaction_type_value_is_required(self):
        with pytest.raises(ParamNotValidated):
            Transaction(
                transaction_id=self.FIXED_ID,
                type_value=None,
                value=1000.0,
                current_balance=2000.0,
                timestamp=1231313112,
            )

    def test_transaction_type_value_is_not_enum(self):
        with pytest.raises(ParamNotValidated):
            Transaction(
                transaction_id=self.FIXED_ID,
                type_value="Withdraw",
                value=1000.0,
                current_balance=2000.0,
                timestamp=1231313112,
            )

    def test_transaction_value_is_required(self):
        with pytest.raises(ParamNotValidated):
            Transaction(
                transaction_id=self.FIXED_ID,
                type_value=TransactionTypeEnum.WITHDRAW,
                value=None,
                current_balance=2000.0,
                timestamp=1231313112,
            )

    def test_transaction_value_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Transaction(
                transaction_id=self.FIXED_ID,
                type_value=TransactionTypeEnum.WITHDRAW,
                value="test",
                current_balance=2000.0,
                timestamp=1231313112,
            )

    def test_transaction_value_is_positive(self):
        with pytest.raises(ParamNotValidated):
            Transaction(
                transaction_id=self.FIXED_ID,
                type_value=TransactionTypeEnum.WITHDRAW,
                value=-1,
                current_balance=2000.0,
                timestamp=1231313112,
            )

    def test_transaction_current_balance_is_required(self):
        with pytest.raises(ParamNotValidated):
            Transaction(
                transaction_id=self.FIXED_ID,
                type_value=TransactionTypeEnum.WITHDRAW,
                value=1000.0,
                current_balance=None,
                timestamp=1231313112,
            )

    def test_transaction_current_balance_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Transaction(
                transaction_id=self.FIXED_ID,
                type_value=TransactionTypeEnum.WITHDRAW,
                value=1000.0,
                current_balance="test",
                timestamp=1231313112,
            )

    def test_transaction_current_balance_is_not_negative(self):
        with pytest.raises(ParamNotValidated):
            Transaction(
                transaction_id=self.FIXED_ID,
                type_value=TransactionTypeEnum.WITHDRAW,
                value=1000.0,
                current_balance=-1.0,
                timestamp=1231313112,
            )

    def test_transaction_timestamp_is_required(self):
        with pytest.raises(ParamNotValidated):
            Transaction(
                transaction_id=self.FIXED_ID,
                type_value=TransactionTypeEnum.WITHDRAW,
                value=1000.0,
                current_balance=2000.0,
                timestamp=None,
            )

    def test_transaction_timestamp_is_not_int(self):
        with pytest.raises(ParamNotValidated):
            Transaction(
                transaction_id=self.FIXED_ID,
                type_value=TransactionTypeEnum.WITHDRAW,
                value=1000.0,
                current_balance=2000.0,
                timestamp=1231313112.0,
            )

    def test_transaction_timestamp_is_positive(self):
        with pytest.raises(ParamNotValidated):
            Transaction(
                transaction_id=self.FIXED_ID,
                type_value=TransactionTypeEnum.WITHDRAW,
                value=1000.0,
                current_balance=2000.0,
                timestamp=-1231313112,
            )
