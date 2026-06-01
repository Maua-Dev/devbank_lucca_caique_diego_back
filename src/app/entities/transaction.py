from typing import Tuple
import uuid
from src.app.errors.entity_errors import ParamNotValidated
from src.app.enums.transaction_type_enum import TransactionTypeEnum


class Transaction:
    transaction_id: str = None
    type_value: TransactionTypeEnum = None
    value: float = None
    current_balance: float = None
    timestamp: int = None
    
    def __init__(
        self,
        transaction_id: str = None,
        type_value: TransactionTypeEnum = None,
        value: float = None,
        current_balance: float = None,
        timestamp: int = None,
    ):
        validation_transaction_id = self.validate_transaction_id(transaction_id)
        if validation_transaction_id[0] is False:
            raise ParamNotValidated("transaction_id", validation_transaction_id[1])
        self.transaction_id = transaction_id

        validation_type = self.validate_type_value(type_value)
        if validation_type[0] is False:
            raise ParamNotValidated("type_value", validation_type[1])
        self.type_value = type_value

        validation_value = self.validate_value(value)
        if validation_value[0] is False:
            raise ParamNotValidated("value", validation_value[1])
        self.value = value

        validation_current_balance = self.validate_current_balance(current_balance)
        if validation_current_balance[0] is False:
            raise ParamNotValidated("current_value", validation_value[1])
        self.current_balance = current_balance

        validation_timestamp = self.validate_timestamp(timestamp)
        if validation_timestamp[0] is False:
            raise ParamNotValidated("timestamp", validation_timestamp[1])
        self.timestamp = timestamp

    @staticmethod
    def validate_transaction_id(transaction_id: str | None) -> Tuple[bool, str]:
        if transaction_id is None:
            return (False, "transaction_id is required")
        if type(transaction_id) is not str:
            return (False, "transaction_id must be a string")
        if not uuid.UUID(transaction_id):
            return (False, "transaction_id must be a valid uuid string")
        return (True, "")

    @staticmethod
    def validate_type_value(type_value: TransactionTypeEnum | None) -> Tuple[bool, str]:
        if type_value is None:
            return (False, "type_value is required")
        if type(type_value) is not TransactionTypeEnum:
            return (False, "type_value must be a Deposit or Withdraw")
        return (True, "")

    @staticmethod
    def validate_value(value: float | None) -> Tuple[bool, str]:
        if value is None:
            return (False, "value is required")
        if type(value) is not float:
            return (False, "value must be a float")
        if value <= 0:
            return (False, "value must be higher than 0")
        return (True, "")

    @staticmethod
    def validate_current_balance(current_balance: float | None) -> Tuple[bool, str]:
        if current_balance is None:
            return (False, "current_balance is required")
        if type(current_balance) is not float:
            return (False, "current_balance must be a float")
        if current_balance < 0:
            return (False, "current_balance must be higher than 0")
        return (True, "")

    @staticmethod
    def validate_timestamp(timestamp: int | None) -> Tuple[bool, str]:
        if timestamp is None:
            return (False, "timestamp is required")
        if type(timestamp) is not int:
            return (False, "timestamp must be a int")
        if timestamp < 0:
            return (False, "timestamp must be higher than 0")
        return (True, "")

    @staticmethod
    def validate_request(request: dict | None) -> Tuple[bool, str]:
        if request is None:
            return (False, "Request is required")
        if type(request) is not dict:
            return (False, "Request must be a dict")
        return (True, "")

    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "type_value": self.type_value,
            "value": self.value,
            "current_balance": self.current_balance,
            "timestamp": self.timestamp,
        }

    def __eq__(self, other):
        return (
            self.type_value == other.type_value
            and self.value == other.value
            and self.current_balance == other.current_balance
            and self.timestamp == other.timestamp
        )

    def __repr__(self):
        return f"""
            Transaction(type_value={self.type_value},
            value={self.value},
            current_balance={self.current_balance})
            timestamp={self.timestamp},
        """
