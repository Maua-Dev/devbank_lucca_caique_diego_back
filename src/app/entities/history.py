class History:
    type: str
    value: float
    current_balance: float
    timestamp: float


    @staticmethod
    def validate_type(type: str) -> Tuple[bool, str]:
        if type is None:
            return (False, "Type is required")
        if type(type) != str:
            return (False, "Type must be a string")
        return (True, "")
    
    @staticmethod
    def validate_value(value: float) -> Tuple[bool, str]:
        if value is None:
            return (False, "Value is required")
        if type(value) != float:
            return (False, "Value must be a float")
        if value < 0:
            return (False, "Value must be a positive number")
        return (True, "")
    
    @staticmethod
    def current_balance(current_balance: float) -> Tuple[bool, str]:
        if current_balance is None:
            return (False, "Current balance is required")
        if type(current_balance) != float:
            return (False, "Current balance must be a float")
        return (True, "")
    
    @staticmethod
    def validate_timestamp(timestamp: float) -> Tuple[bool, str]:
        if timestamp is None:
            return (False, "Timestamp is required")
        if type(timestamp) != float:
            return (False, "Timestamp must be a float")
        return (True, "")
    