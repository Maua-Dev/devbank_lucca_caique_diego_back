from abc import ABC, abstractmethod
from typing import List, Optional
from src.app.entities.history import History


class IHistoryRepository(ABC):
    @abstractmethod
    def get_all_historys(self) -> List[History]:
        """
        Return all stored historys.

        Returns:
            List[History]: Collection of all historys currently persisted.
        """
        pass

    @abstractmethod
    def get_history(self, history_id: str) -> Optional[History]:
        """
        Retrieve a single history by its identifier.

        Args:
            history_id (str): UUID string stored in the entity attribute `history.history_id`.

        Returns:
            Optional[History]: The matching history when found, otherwise `None`.
        """
        pass

    @abstractmethod
    def create_history(self, history: History) -> History:
        """
        Persist a new history.

        Args:
            history (History): Fully validated history entity.

        Returns:
            History: The persisted history.
        """
        pass

    @abstractmethod
    def delete_history(self, history_id: str) -> Optional[History]:
        """
        Delete an history by its identifier.

        Args:
            history_id (str): UUID string of the target history.

        Returns:
            Optional[History]: Deleted history when found, otherwise `None`.
        """
        pass

    @abstractmethod
    def update_history(
        self,
        history_id: str = None,
        type: str = None, 
        value: float = None, 
        current_balance: float = None,
        timestamp: float = None 
    ) -> Optional[History]:
        """
        Update mutable fields of an existing history.

        Args:
            history_id (str): UUID string of the history to update.
            type (str, optional): New type.
            value (float, optional): New value.
            current_balance (float, optional): New current balance.
            timestamp(float, optional): New timestamp.

        Returns:
            Optional[History]: Updated history when found, otherwise `None`.
        """
        pass