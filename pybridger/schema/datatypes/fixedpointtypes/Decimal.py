#-------------------------------------------------------------------------------
from typing                     import Any
from .FixedPointType            import FixedPointType
from ....common                 import override
from ....common                 import private
from ....common                 import public
from ....mapper                 import Query
#-------------------------------------------------------------------------------
class Decimal(FixedPointType):
    """
    Define fixed point class.
    
    MySQL query      : "DECIMAL(M, D)"
    Sqlite3 query    : "DECIMAL(M, D)"
    PostgreSQL query : "DECIMAL(M, D)"
    """
    #---------------------------------------------------------------------------
    def __init__(
            self,
            M          : int,
            D          : int,
        ) -> None:
        """
        Initialize fixed point object
        Args:
            M          (int)  : decimal digits (supported sql MySQL, PostgreSQL)
            D          (int)  : scale (supported sql MySQL, PostgreSQL)
            ```
            # Used MySQL
            dataType = Decimal(2, 3)
            # Used Sqlite3
            dataType = Decimal(2, 3)
            # Used PostgreSQL
            dataType = Decimal(2, 3)
            ```
        """
        super().__init__()
        self.M = M
        self.D = D
    #---------------------------------------------------------------------------
    @private
    def __buildMySqlQuery(self) -> Query:
        """
        Build query by MySQL
        Returns:
            Query : query "DECIMAL"
        """
        return Query(f"DECIMAL({self.M}, {self.D})")
    #---------------------------------------------------------------------------
    @private
    def __buildSqlite3(self) -> Query:
        """
        Build query by Sqlite3
        Returns:
            Query : query "DECIMAL"
        """
        return Query(f"DECIMAL")
    #---------------------------------------------------------------------------
    @public
    def __buildPostgreSqlQuery(self) -> Query:
        """
        Build query by PostgreSQL
        Returns:
            Query : query "DECIMAL"
        """
        return Query(f"DECIMAL({self.M}, {self.D})")
    #---------------------------------------------------------------------------
    @override
    @public
    def mysql(self) -> None:
        self.query : Any = self.__buildMySqlQuery()
    #---------------------------------------------------------------------------
    @override
    @public
    def sqlite3(self) -> None:
        self.query : Any = self.__buildSqlite3()
    #---------------------------------------------------------------------------
    @override
    @public
    def postgresql(self) -> None:
        self.query : Any = self.__buildPostgreSqlQuery()
#-------------------------------------------------------------------------------