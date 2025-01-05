from dataclasses import dataclass, field
from uuid import UUID, uuid1

@dataclass
class Expense:
    """
    出費を表すデータクラス。

    Attributes:
        description (str): 出費の説明。
        amount (float): 出費の金額。
        id (UUID): 出費のユニークID。デフォルトは `uuid1()` を使用。
    """
    description: str
    amount: float
    id: UUID = field(default_factory=uuid1)
