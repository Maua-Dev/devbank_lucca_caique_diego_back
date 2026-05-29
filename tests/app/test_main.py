import src.app.main as main_module
from src.app.main import execute_get_pra_barra
from src.app.repo.member_repository_mock import MemberRepositoryMock


class Test_Main:
    FIRST_MEMBER_ID = "b11af449-22c7-43db-b0e4-dbfbbe7fdbd7"

    def setup_method(self):
        main_module.member_repo = MemberRepositoryMock()

    def test_execute_get_pra_barra(self):
        repo = MemberRepositoryMock()
        response = execute_get_pra_barra()
        expected_member = repo.get_first_member()
        assert response == {
            "member_id": self.FIRST_MEMBER_ID,
            "member": expected_member.to_dict(),
        }
