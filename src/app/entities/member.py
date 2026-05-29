import uuid
from src.app.errors.entity_errors import ParamNotValidated
from typing import Tuple
import re


class Member:
    member_id: str
    name: str
    agency: str
    account: str
    current_balance: float

    def __init__(
        self,
        member_id: str = None,
        name: str = None,
        agency: str = None,
        account: str = None,
        current_balance: float = None,
    ):

        validation_member_id = self.validade_member_id(member_id)
        if validation_member_id[0] is False:
            raise ParamNotValidated("member_id", validation_member_id[1])
        self.member_id = member_id

        validation_name = self.validate_name(name)
        if validation_name[0] is False:
            raise ParamNotValidated("name", validation_name[1])
        self.name = name

        validation_agency = self.validate_agency(agency)
        if validation_agency[0] is False:
            raise ParamNotValidated("agency", validation_agency[1])
        self.agency = agency

        validation_account = self.validate_account(account)
        if validation_account[0] is False:
            raise ParamNotValidated("account", validation_account[1])
        self.account = account

        validation_current_balance = self.validade_current_balance(current_balance)
        if validation_current_balance[0] is False:
            raise ParamNotValidated("current_balance", validation_current_balance[1])
        self.current_balance = current_balance

    @staticmethod
    def validade_member_id(member_id: str) -> Tuple[bool, str]:
        if member_id is None:
            return (False, "member_id is required")
        if type(member_id) is not str:
            return (False, "member_id must be a string")
        if not uuid.UUID(member_id):
            return (False, "member_id must be a valid uuid string")
        return (True, "")

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
        if not re.fullmatch(r"\d{4}", agency):
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
        if not re.fullmatch(r"^\d{5}-\d$", account):
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
            "member_id": self.member_id,
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
