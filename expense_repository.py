from abc import ABC, abstractmethod
from uuid import UUID
from expense import Expense

class ExpenseRepository(ABC):
    """
    出費リポジトリの抽象基底クラス。
    """

    @abstractmethod
    def find(self, id: UUID) -> Expense:
        """
        ユニークな識別子で出費を検索します。

        :param id: 検索する出費のUUID。
        :return: 指定されたIDの出費。
        """
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> list[Expense]:
        """
        すべての出費を検索します。

        :return: すべての出費のリスト。
        """
        raise NotImplementedError

    @abstractmethod
    def insert(self, expense: Expense) -> None:
        """
        新しい出費をリポジトリに挿入します。

        :param expense: 挿入する出費。
        """
        raise NotImplementedError
    
    @abstractmethod
    def update(self, expense: Expense) -> None:
        """
        リポジトリ内の既存の出費を更新します。

        :param expense: 更新する出費。
        """
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, expense: Expense) -> None:
        """
        リポジトリから出費を削除します。

        :param expense: 削除する出費。
        """
        raise NotImplementedError
