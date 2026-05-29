from abc import ABC, abstractmethod
from typing import List, Optional

from src.app.entities.member import Member


class IMemberRepository(ABC):
    @abstractmethod
    def get_first_member(self) -> List[Member]:
        """
        Return the first member stored.

        Returns:
            Member: The first member currently persisted.
        """
        pass

    @abstractmethod
    def get_all_members(self) -> List[Member]:
        
        """
        Return all stored members.

        Returns:
            List[Member]: Collection of all member currently persisted.
        """
        pass
    
    @abstractmethod
    def get_member(self, member_id : str) -> Optional[Member]:
        """
        Retrieve a single member by member identifier.

        Args:
            member_id (str): UUID string stored in the entity attribute ⁠ Member.member_id ⁠.

        Returns:
            Optional[Member]: The matching member when found, otherwise ⁠ None ⁠.
        """
        pass

    @abstractmethod
    def create_member(self, member: Member) -> Member:
        """
        Persist a new member.

        Args:
            member (Member): Fully validated member entity.

        Returns:
            Member: The persisted member.
        """
        pass

    @abstractmethod
    def delete_member(self, member_id: str) -> Optional[Member]:
        """
        Delete an member by its identifier.

        Args:
            member_id (str): UUID string of the target member.

        Returns:
            Optional[Member]: Deleted member when found, otherwise ⁠ None ⁠.
        """
        pass
    
    @abstractmethod
    def update_member(
        self,
        member_id: str = None,
        name: str = None,
        agency: str = None,
        account: str = None,
        current_balance: float = None,
    ) -> Optional[Member]:
        """
        Update mutable fields of an existing member.

        Args:
            member_id (str): UUID string of the member to update.
            name (str): New name.
            agency (str): New agency.
            account (str): New account.
            current_balance (float): New current balance.

        Returns:
            Optional[Member]: Updated member when found, otherwise ⁠ None ⁠.
        """
        pass