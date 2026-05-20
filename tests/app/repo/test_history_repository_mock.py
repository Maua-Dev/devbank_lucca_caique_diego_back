from src.app.entities.history import History
from src.app.repo.history_repository_mock import HistoryRepositoryMock

class Test_HistoryRepositoryMock:
    FIRST_HISTORY_ID = "b11af449-22c7-43db-b0e4-dbfbbe7fdbd7"
    NOT_FOUND_HISTORY_ID = "00000000-0000-0000-0000-000000000000"
    CREATED_HISTORY_ID = "88f0920c-0de0-4e0a-bb46-abdb3705579d"

    def test_get_all_historys(self):
        repo = HistoryRepositoryMock()
        historys = repo.get_all_historys()
        assert len(historys) == len(repo.historys)
        assert all([history_expect == history for history_expect, history in zip(repo.historys, historys)])
        
    def test_get_history(self):
        repo = HistoryRepositoryMock()
        history = repo.get_history(history_id=self.FIRST_HISTORY_ID)
        assert history is not None
        assert history.history_id == self.FIRST_HISTORY_ID
    
    def test_get_history_not_found(self):
        repo = HistoryRepositoryMock()
        history = repo.get_history(history_id=self.NOT_FOUND_HISTORY_ID)
        assert history is None
        
    def test_create_history(self):
        repo = HistoryRepositoryMock()
        len_before = len(repo.historys)
        history = History(
            history_id=self.CREATED_HISTORY_ID,
            type_value="Deposit",
            value=500.0,
            current_balance=1000.0,
            timestamp=5.0,
        )
        repo.create_history(history=history)
        len_after = len(repo.historys)
        assert len_after == len_before + 1
        assert repo.historys[-1] == history
        assert repo.historys[-1].history_id == self.CREATED_HISTORY_ID
        
    def test_delete_history(self):
        repo = HistoryRepositoryMock()
        history_expected_to_be_deleted = repo.get_history(self.FIRST_HISTORY_ID)
        len_before = len(repo.historys)
        
        history = repo.delete_history(history_id=self.FIRST_HISTORY_ID)
        len_after = len(repo.historys)
        assert len_after == len_before - 1
        assert history == history_expected_to_be_deleted
        assert repo.get_history(self.FIRST_HISTORY_ID) is None
        
    def test_delete_history_not_found(self):
        repo = HistoryRepositoryMock()
        history = repo.delete_history(history_id=self.NOT_FOUND_HISTORY_ID)
        assert history is None
        
    def test_update_history(self):
        repo = HistoryRepositoryMock()
        history_updated = repo.update_history(
            history_id=self.FIRST_HISTORY_ID,
            type_value="Deposit",
            value=500.0,
            current_balance=1000.0,
            timestamp=5.0,
        )
        
        assert history_updated is not None
        assert history_updated.history_id == self.FIRST_HISTORY_ID
        assert history_updated.type_value == "Deposit"
        assert history_updated.value == 500.0
        assert history_updated.current_balance == 1000.0
        assert history_updated.timestamp == 5.0
        
    def test_update_history_type_value(self):
        repo = HistoryRepositoryMock()
        type_value = "Deposit"
        history_updated = repo.update_history(history_id=self.FIRST_HISTORY_ID, type_value=type_value)
        
        assert history_updated.type_value == type_value
        assert repo.get_history(self.FIRST_HISTORY_ID).type_value == type_value
        
    def test_update_history_value(self):
        repo = HistoryRepositoryMock()
        value = 500.0
        history_updated = repo.update_history(history_id=self.FIRST_HISTORY_ID, value=value)
        
        assert history_updated.value == value
        assert repo.get_history(self.FIRST_HISTORY_ID).value == value