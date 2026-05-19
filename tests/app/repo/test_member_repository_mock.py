from src.app.entities.member import Member
from src.app.repo.member_repository_mock import MemberRepositoryMock


class Test_MemberRepositoryMock:
    FIRST_MEMBER_ID = "b11af449-22c7-43db-b0e4-dbfbbe7fdbd7"
    NOT_FOUND_MEMBER_ID = "00000000-0000-0000-0000-000000000000"
    CREATED_MEMBER_ID = "88f0920c-0de0-4e0a-bb46-abdb3705579d"

    def test_get_all_members(self):
        repo = MemberRepositoryMock()
        members = repo.get_all_members()
        assert len(members) == len(repo.members)
        assert all(
            [
                member_expect == member
                for member_expect, member in zip(repo.members, members)
            ]
        )

    def test_get_member(self):
        repo = MemberRepositoryMock()
        member = repo.get_member(member_id=self.FIRST_MEMBER_ID)
        assert member is not None
        assert member.member_id == self.FIRST_MEMBER_ID

    def test_get_member_not_found(self):
        repo = MemberRepositoryMock()
        member = repo.get_member(member_id=self.NOT_FOUND_MEMBER_ID)
        assert member is None

    def test_create_member(self):
        repo = MemberRepositoryMock()
        len_before = len(repo.members)
        member = Member(
            member_id=self.CREATED_MEMBER_ID,
            name="Roberto",
            agency="1234",
            account="12345-6",
            current_balance=45000.0,
        )
        repo.create_member(member=member)
        len_after = len(repo.members)
        assert len_after == len_before + 1
        assert repo.members[-1] == member
        assert repo.members[-1].member_id == self.CREATED_MEMBER_ID

    def test_delete_member(self):
        repo = MemberRepositoryMock()
        member_expected_to_be_deleted = repo.get_member(self.FIRST_MEMBER_ID)
        len_before = len(repo.members)

        member = repo.delete_member(member_id=self.FIRST_MEMBER_ID)
        len_after = len(repo.members)
        assert len_after == len_before - 1
        assert member == member_expected_to_be_deleted
        assert repo.get_member(self.FIRST_MEMBER_ID) is None

    def test_delete_member_not_found(self):
        repo = MemberRepositoryMock()
        member = repo.delete_member(member_id=self.NOT_FOUND_MEMBER_ID)
        assert member is None

    def test_update_member(self):
        repo = MemberRepositoryMock()
        member_updated = repo.update_member(
            member_id=self.FIRST_MEMBER_ID,
            name="Roberto",
            agency="1234",
            account="12345-6",
            current_balance=45000,
        )

        assert member_updated is not None
        assert member_updated.member_id == self.FIRST_MEMBER_ID
        assert member_updated.name == "Roberto"
        assert member_updated.agency == "1234"
        assert member_updated.account == "12345-6"
        assert member_updated.current_balance == 45000

    def test_update_member_name(self):
        repo = MemberRepositoryMock()
        name = "Roberto"
        member_updated = repo.update_member(member_id=self.FIRST_MEMBER_ID, name=name)

        assert member_updated.name == name
        assert repo.get_member(self.FIRST_MEMBER_ID).name == name

    def test_update_member_agency(self):
        repo = MemberRepositoryMock()
        agency="1234"
        member_updated = repo.update_member(member_id=self.FIRST_MEMBER_ID, agency=agency)

        assert member_updated.agency == agency
        assert repo.get_member(self.FIRST_MEMBER_ID).agency == agency
