#-------------------------------------------------------------------------------
from typing                     import Any
from .FixedPointType            import FixedPointType
from ....common                 import override
from ....common                 import private
from ....common                 import public
from ....mapper                 import Query
#-------------------------------------------------------------------------------
class Numeric(FixedPointType):
    """
    Define fixed point class.
    
    MySQL query      : "NUMERIC(M, D)"
    Sqlite3 query    : "NUMERIC(M, D)"
    PostgreSQL query : "NUMERIC(M, D)"
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
            M          (int)  : decimal digits 
            D          (int)  : scale
            ```
            # Used MySQL
            dataType = Numeric(2, 3)
            # Used Sqlite3
            dataType = Numeric(2, 3)
            # Used PostgreSQL
            dataType = Numeric(2, 3)
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
            Query : query "NUMERIC"
        """
        return Query(f"NUMERIC({self.M}, {self.D})")
    #---------------------------------------------------------------------------
    @private
    def __buildSqlite3(self) -> Query:
        """
        Build query by Sqlite3
        Returns:
            Query : query "NUMERIC"
        """
        return Query(f"NUMERIC({self.M}, {self.D})")
    #---------------------------------------------------------------------------
    @private
    def __buildPostgreSqlQuery(self) -> Query:
        """
        Build query by PostgreSQL
        Returns:
            Query : query "NUMERIC"
        """
        return Query(f"NUMERIC({self.M}, {self.D})")
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