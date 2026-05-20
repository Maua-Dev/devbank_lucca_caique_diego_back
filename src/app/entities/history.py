from typing import Tuple
import uuid
from src.app.errors.entity_errors import ParamNotValidated

class History:
    history_id: str
    type_value: str
    value: float
    current_balance: float
    timestamp: float

    def __init__(
        self,
        history_id: str = None,
        type_value: str = None, 
        value: float = None, 
        current_balance: float = None,
        timestamp: float = None 
    ):
        validation_history_id = History.validate_history_id(history_id)  # Corrigido
        if validation_history_id[0] is False:
            raise ParamNotValidated("history_id", validation_history_id[1])
        self.history_id = history_id
        
        validation_type = History.validate_type(type_value=type_value)  # Corrigido
        if validation_type[0] is False:
            raise ParamNotValidated("type_value", validation_type[1])  
        self.type_value = type_value  

        validation_value = History.validate_value(value)  # Corrigido
        if validation_value[0] is False:
            raise ParamNotValidated("value", validation_value[1])
        self.value = value

        validation_current_balance = History.validate_current_balance(current_balance)  # Corrigido
        if validation_current_balance[0] is False:
            raise ParamNotValidated("current_value", validation_value[1])
        self.current_balance = current_balance

        validation_timestamp = History.validate_timestamp(timestamp)  # Corrigido
        if validation_timestamp[0] is False:
            raise ParamNotValidated("timestamp", validation_timestamp[1])
        self.timestamp = timestamp
            
    @staticmethod
    def validade_history_id(history_id: str) -> Tuple[bool, str]:
        if history_id is None:
            return (False, "history_id is required")
        if type(history_id) is not str:
            return (False, "history_id must be a string")
        if not uuid.UUID(history_id):
            return (False, "history_id must be a valid uuid string")
        return (True, "")

    @staticmethod
    def validate_type_value(type_value: str) -> Tuple[bool, str]:
        if type_value is None:
            return (False, "type_value is required")
        if type(type_value) is not str:
            return (False, "type_value must be a string")
        if len(type_value) < 3:
            return (False, "type_value must have at least 3 characters")
        return (True, "")

    @staticmethod
    def validade_value(value: float) -> Tuple[bool, str]:
        if value is None:
            return (False, "value is required")
        if type(value) is not float:
            return (False, "value must be a float")
        if value < 0:
            return (False, "value must be higher than 0")
        return (True, "")

    @staticmethod
    def validade_current_balance(current_balance: float) -> Tuple[bool, str]:
        if current_balance is None:
            return (False, "current_balance is required")
        if type(current_balance) is not float:
            return (False, "current_balance must be a float")
        if current_balance < 0:
            return (False, "current_balance must be higher than 0")
        return (True, "")

    @staticmethod
    def validade_timestamp(timestamp: float) -> Tuple[bool, str]:
        if timestamp is None:
            return (False, "timestamp is required")
        if type(timestamp) is not float:
            return (False, "timestamp must be a float")
        if timestamp < 0:
            return (False, "timestamp must be higher than 0")
        return (True, "")

    def to_dict(self):
        return {
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
            History(type_value={self.type_value},
            value={self.value},
            current_balance={self.current_balance})
            timestamp={self.timestamp},
        """
