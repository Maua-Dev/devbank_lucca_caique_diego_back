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
            member_id (str): Name string stored in the entity attribute `Member.name`.

        Returns:
            Optional[Member]: The matching member when found, otherwise None.
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
        name: str | None = None,
        agency: str | None = None,
        account: str | None = None,
        current_balance: float | None = None,
    ) -> Optional[Member]:
        """
        Update mutable fields of an existing member.

        Args:
            name (str): Name string stored in the entity attribute `Member.name`.
            agency (str): Agency string stored in the entity attribute `Member.agency`.
            account (str): Account string stored in the entity attribute `Member.account`.
            current_balance (float): Current balance float stored in the entity attribute `Member.current_balance`.

        Returns:
            Optional[Member]: Updated member when found, otherwise ⁠ None ⁠.
        """
        pass