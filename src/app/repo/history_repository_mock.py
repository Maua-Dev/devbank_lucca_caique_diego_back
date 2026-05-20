from typing import Optional, List
from src.app.entities.history import History
from src.app.repo.history_repository_interface import IHistoryRepository


class HistoryRepositoryMock(IHistoryRepository):
    historys: List[History]

    def __init__(self):
        self.historys = [
            History(
                history_id="b11af449-22c7-43db-b0e4-dbfbbe7fdbd7",
                type_value="Deposity",
                value=550.0,
                current_balance=1200.0,
                timestamp=2.0,
            ),
            History(
                history_id="b21af449-22c7-43db-b0e4-dbfbbe7fdbd7",
                type_value="Withdraw",
                value=1000.0,
                current_balance=1200.0,
                timestamp=2.0,
            ),
        ]

    def get_all_historys(self) -> List[History]:
        return self.historys

    def get_history(self, history_id: str) -> Optional[History]:
        for history in self.historys:
            if history.history_id == history_id:
                return history

        return None

    def create_history(self, history: History) -> History:

        self.historys.append(history)

        return history

    def delete_history(self, history_id: str) -> History:
        for history in self.historys:
            if history.history_id == history_id:
                self.historys.remove(history)
                return history
        return None

    def update_history(
        self,
        history_id: str,
        type_value: str = None,
        value: float = None,
        current_balance: float = None,
        timestamp: float = None,
    ) -> Optional[History]:

        for history in self.historys:
            if history.history_id == history_id:
                if type_value is not None:
                    history.type_value = type_value
                if value is not None:
                    history.value = value
                if timestamp is not None:
                    history.timestamp = timestamp
                if current_balance is not None:
                    history.current_balance = current_balance
                return history
        return None
