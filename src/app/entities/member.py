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
            return (False, "name is required")
        if type(name) is not str:
            return (False, "name must be a string")
        if len(name) < 3:
            return (False, "name must have at least 3 characters")
        return (True, "")

    @staticmethod
    def validate_agency(agency: str) -> Tuple[bool, str]:
        if agency is None:
            return (False, "agency is required")
        if type(agency) is not str:
            return (False, "agency must be a string")
        if len(agency) != 4:
            return (False, "agency must have 4 characters")
        return (True, "")

    @staticmethod
    def validate_account(account: str) -> Tuple[bool, str]:
        if account is None:
            return (False, "account is required")
        if type(account) is not str:
            return (False, "account must be a string")
        if len(account) != 7:
            return (False, "account must have 7 characters")
        if "-" not in account[-2]:
            return (False, "account must have a - in second to last position")
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

    def to_dict(self):
        return {
            "name": self.name,
            "agency": self.agency,
            "account": self.account,
            "current_balance": self.current_balance,
        }

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.account == other.account
            and self.agency == other.agency
            and self.current_balance == other.current_balance
        )

    def __repr__(self):
        return f"""
            Member(name={self.name},
            agency={self.agency},
            account={self.account},
            current_balance={self.current_balance})
        """
