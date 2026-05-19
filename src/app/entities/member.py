from typing import Tuple


class Member:
    name: str
    agency: str
    account: str
    current_balance: float

    def __init__(
        self,
        name: str = None,
        agency: str = None,
        account: str = None,
        current_balance: float = None,
    ):
        self.name = name
        self.account = account
        self.agency = agency
        self.current_balance = current_balance

    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        if name is None:
            return (False, "Name is required")
        if type(name) is not str:
            return (False, "Name must be a string")
        return (True, "")
    
    @staticmethod
    def validate_agency(agency:str) ->Tuple[bool, str]:
        if agency is None:
            return (False, "Agency is required")
        if type(agency) is not str:
            return (False, "Agency must be a string")
        return (True, "")
