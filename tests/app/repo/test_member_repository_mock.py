from src.app.entities.member import Member
from src.app.repo.member_repository_mock import MemberRepositoryMock


class Test_MemberRepositoryMock:

    def test_get_first_member(self):
        repo = MemberRepositoryMock()
        member = repo.get_first_member()
        assert member is not None
        assert member.name == "Vitor Soller"
        assert member.agency == "0000"
        assert member.account == "00000-0"
        assert member.current_balance == 1000.0
        assert member == repo.members[0]

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
        member = repo.get_member(name="Vitor Soller")
        assert member is not None
        assert member.name == "Vitor Soller"
        assert member.agency == "0000"
        assert member.account == "00000-0"
        assert member.current_balance == 1000.0

    def test_get_member_not_found(self):
        repo = MemberRepositoryMock()
        member = repo.get_member(name="Not found")
        assert member is None

    def test_create_member(self):
        repo = MemberRepositoryMock()
        len_before = len(repo.members)
        member = Member(
            name="Vitor Soller",
            agency="0000",
            account="00000-0",
            current_balance=1000.0,
        )
        repo.create_member(member=member)
        len_after = len(repo.members)
        assert len_after == len_before + 1
        assert repo.members[-1] == member

    def test_delete_member(self):
        repo = MemberRepositoryMock()
        member_expected_to_be_deleted = repo.get_member(name="Vitor Soller")
        len_before = len(repo.members)

        member = repo.delete_member(name="Vitor Soller")
        len_after = len(repo.members)
        assert len_after == len_before - 1
        assert member == member_expected_to_be_deleted
        assert repo.get_member(name="Vitor Soller") is None

    def test_delete_member_not_found(self):
        repo = MemberRepositoryMock()
        member = repo.delete_member(name="Not found")
        assert member is None

    def test_update_member(self):
        repo = MemberRepositoryMock()
        member_updated = repo.update_member(
            name="Vitor Soller",
            agency="0000",
            account="00000-0",
            current_balance=1000.0,
        )

        assert member_updated is not None
        assert member_updated.name == "Vitor Soller"
        assert member_updated.agency == "0000"
        assert member_updated.account == "00000-0"
        assert member_updated.current_balance == 1000.0

    def test_update_member_name(self):
        repo = MemberRepositoryMock()
        name = "Vitor Soller"
        member_updated = repo.update_member(name=name, agency="0000")

        assert member_updated.name == name
        assert member_updated.agency == "0000"
        assert repo.get_member(name=name).name == name
        assert repo.get_member(name=name).agency == "0000"

    def test_update_member_agency(self):
        repo = MemberRepositoryMock()
        agency="0000"
        name = "Vitor Soller"
        member_updated = repo.update_member(name=name, agency=agency, account="00000-0", current_balance=1000.0)

        assert member_updated.agency == agency
        assert repo.get_member(name=name).agency == agency
        assert member_updated.account == "00000-0"
        assert member_updated.current_balance == 1000.0
        assert repo.get_member(name=name).account == "00000-0"
        assert repo.get_member(name=name).current_balance == 1000.0