from typing import Optional, List
from ..entities.member import Member
from .member_repository_interface import IMemberRepository


class MemberRepositoryMock(IMemberRepository):
    members: List[Member]

    def __init__(self):
        self.members = [
            Member(
                name="Caique",
                agency="1305",
                account="13050-7",
                current_balance=1200.0,
            ),
            Member(
                name="Lucca",
                agency="0202",
                account="02020-2",
                current_balance=10000.0,
            ),
            Member(
                name="Diego",
                agency="6769",
                account="67695-1",
                current_balance=505.0,
            ),
        ]

    def get_first_member(self) -> Member:
        return self.members[0]

    def get_all_members(self) -> List[Member]:
        return self.members

    def get_member(self, name: str) -> Optional[Member]:
        for member in self.members:
            if member.name == name:
                return member

        return None

    def create_member(self, member: Member) -> Member:

        self.members.append(member)

        return member

    def delete_member(self, name: str) -> Member:
        for member in self.members:
            if member.name == name:
                self.members.remove(member)
                return member
        return None

    def update_member(
        self,
        name: str | None = None,
        agency: str | None = None,
        account: str | None = None,
        current_balance: float | None = None,
    ) -> Optional[Member]:
        if not self.members:
            return None

        member = self.members[0]

        if name is not None:
            member.name = name
        if agency is not None:
            member.agency = agency
        if account is not None:
            member.account = account
        if current_balance is not None:
            member.current_balance = current_balance

        return member
