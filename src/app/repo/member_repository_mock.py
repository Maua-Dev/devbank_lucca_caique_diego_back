from ast import List
from typing import Optional
from src.app.entities.member import Member
from src.app.repo.member_repository_interface import IMemberRepository


class MemberRepositoryMock(IMemberRepository):
    members: List[Member]

    def __init__(self):
        self.members = [
            Member(
                member_id="b11af449-22c7-43db-b0e4-dbfbbe7fdbd7",
                name="Caique",
                agency="1305",
                account="13050-7",
                current_balance=2750,
            ),
            Member(
                member_id="b21af449-22c7-43db-b0e4-dbfbbe7fdbd7",
                name="Lucca",
                agency="0202",
                account="02020-2",
                current_balance=10.000,
            ),
            Member(
                member_id="b31af449-22c7-43db-b0e4-dbfbbe7fdbd7",
                name="Diego",
                agency="6769",
                account="67695-1",
                current_balance=505,
            ),
        ]

    def get_all_member(self) -> List[Member]:
        return self.members

    def get_member(self, member_id: str) -> Optional[Member]:
        for member in self.members:
            if member.member_id == member_id:
                return member

        return None

    def create_member(self, member: Member) -> Member:

        self.members.append(member)

        return member

    def delete_member(self, member_id: str) -> Member:
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                return member
        return None

    def update_member(
        self,
        member_id: str,
        name: str = None,
        agency: str = None,
        account: str = None,
        current_balance: float = None,
    ) -> Optional[Member]:

        for member in self.members:
            if member.member_id == member_id:
                if name is not None:
                    member.name = name
                if agency is not None:
                    member.agency = agency
                if account is not None:
                    member.account = account
                if current_balance is not None:
                    member.current_balance = current_balance
                return member
        return None
