import pytest
from src.app.entities.member import Member
from src.app.errors.entity_errors import ParamNotValidated


class Test_Member:
    def test_member(self):
        member = Member(
            name="test",
            agency="0000",
            account="00000-0",
            current_balance=1000.0,
        )
        assert member.name == "test"
        assert member.agency == "0000"
        assert member.account == "00000-0"
        assert member.current_balance == 1000.0

    def test_member_name_is_required(self):
        with pytest.raises(ParamNotValidated):
            Member(
                name=None,
                agency="0000",
                account="00000-0",
                current_balance=1000.0,
            )

    def test_member_name_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            Member(
                name=1,
                agency="0000",
                account="00000-0",
                current_balance=1000.0,
            )

    def test_member_name_is_too_short(self):
        with pytest.raises(ParamNotValidated):
            Member(
                name="aa",
                agency="0000",
                account="00000-0",
                current_balance=1000.0,
            )

    def test_member_agency_is_required(self):
        with pytest.raises(ParamNotValidated):
            Member(
                name="test",
                agency=None,
                account="00000-0",
                current_balance=1000.0,
            )

    def test_member_agency_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            Member(
                name="test",
                agency=123,
                account="00000-0",
                current_balance=1000.0,
            )

    def test_member_agency_is_too_short(self):
        with pytest.raises(ParamNotValidated):
            Member(
                name="test",
                agency="000",
                account="00000-0",
                current_balance=1000.0,
            )

    def test_member_account_is_required(self):
        with pytest.raises(ParamNotValidated):
            Member(
                name="test",
                agency="0000",
                account=None,
                current_balance=1000.0,
            )

    def test_member_account_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            Member(
                name="test",
                agency="0000",
                account=1233,
                current_balance=1000.0,
            )

    def test_member_account_is_too_short(self):
        with pytest.raises(ParamNotValidated):
            Member(
                name="test",
                agency="0000",
                account="00000-",
                current_balance=1000.0,
            )

    def test_member_account_has_signal(self):
        with pytest.raises(ParamNotValidated):
            Member(
                name="test",
                agency="0000",
                account="0000000",
                current_balance=1000.0,
            )

    def test_member_current_balance_is_required(self):
        with pytest.raises(ParamNotValidated):
            Member(
                name="test",
                agency="0000",
                account="00000-0",
                current_balance=None,
            )

    def test_member_current_balance_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Member(
                name="test",
                agency="0000",
                account="00000-0",
                current_balance="12312",
            )

    def test_member_current_balance_is_negative(self):
        with pytest.raises(ParamNotValidated):
            Member(
                name="test",
                agency="0000",
                account="00000-0",
                current_balance=-1,
            )
