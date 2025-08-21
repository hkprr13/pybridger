# -------------------------------------------------------------------------------
from .Constraint    import Constraint
from ...common      import override
from ...common      import public
from ...mapper      import Query
# -------------------------------------------------------------------------------
class TableLevelCheck(Constraint):
    """
    Defined table-level check constraint
    """
# 
    def __init__(
        self,
        *conditons: tuple[str]
    ) -> None:
        """
        Initialize table-level check constraint object
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
        """
        Build query for table-level check constraint 
        Returns:
            Query: 
        """
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
