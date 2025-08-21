# -------------------------------------------------------------------------------
from .Constraints import Constraints  # 基底クラス
from ...common import override     # オーバライドデコレーター
from ...common import public       # パブリックデコレーター
from ...mapper import Query        # クエリクラス
# -------------------------------------------------------------------------------


class TableLevelCheck(Constraints):
    """
    Defined table-level check constraints
    """
# 
    def __init__(
        self,
        *conditons: tuple[str]
    ) -> None:
        """
        Initialize table-level check constraints object
        
        Args:
            conditons (tuple[str]) : Conditional expressions specified as strings.

        Examples:
            ```
            class Employees(Model):
                salary = Column(
                    dataType = Integer()
                )
                bonus  = Column(
                    dataType        = Integer(),
                    tableLevelCheck = "bonus <= salary * 0.5"
                )
            ```
        """

        self.__conditions = conditons
    # ---------------------------------------------------------------------------

    @public
    def __buildTableLevelCheckQuery(self) -> Query:
        query = ""
        for cond in self.__conditions:
            query += f"CHECK ({cond}),"
        query = query[:-1]
        return Query(query)
    # ---------------------------------------------------------------------------

    @override
    def mysql(self) -> None:
        self.query = self.__buildTableLevelCheckQuery()
    # ---------------------------------------------------------------------------

    @override
    def sqlite3(self) -> None:
        self.query = self.__buildTableLevelCheckQuery()
    # ---------------------------------------------------------------------------

    @override
    def postgresql(self) -> None:
        self.query = self.__buildTableLevelCheckQuery()
# -------------------------------------------------------------------------------
