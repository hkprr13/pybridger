#-------------------------------------------------------------------------------
from typing                     import Any
from .FloatingPointDataType     import FloatingPointDataType
from ....common                 import override
from ....common                 import private
from ....mapper                 import Query
#-------------------------------------------------------------------------------
class Real(FloatingPointDataType):
    """
    Define double precision Real point class.
    
    MySQL query      : "REAL"
    Sqlite3 query    : "REAL"
    PostgreSQL query : "REAL"
    """
    def __init__(self) -> None:
        """
        Initialize double precision Real point object
        Args:

        Examples:
            ```
            # Used MySQL
            dataType = Real()
            # Used Sqlite3
            dataType = Real()
            # Used PostgreSQL
            dataType = Real()
            ```
        """
        super().__init__()
    #---------------------------------------------------------------------------
    @private
    def __buildMySqlQuery(self) -> Query:
        """
        Build query by MySQL
        Returns:
            Query : query "REAL"
        """
        return Query("REAL")
    #---------------------------------------------------------------------------
    @private
    def __buildSqlite3(self) -> Query:
        """
        Build query by Sqlite3
        Returns:
            Query : query "REAL"
        """
        return Query("REAL")
    #---------------------------------------------------------------------------
    @private
    def __buildPostgreSqlQuery(self) -> Query:
        """
        Build query by PostgreSQL
        Returns:
            Query : query "REAL"
        """
        return Query("REAL")
    #---------------------------------------------------------------------------
    @override
    @private
    def mysql(self) -> None:
        self.query : Any = self.__buildMySqlQuery()
    #---------------------------------------------------------------------------
    @override
    @private
    def sqlite3(self) -> None:
        self.query : Any = self.__buildSqlite3()
    #---------------------------------------------------------------------------
    @override
    @private
    def postgresql(self) -> None:
        self.query : Any = self.__buildPostgreSqlQuery()
#-------------------------------------------------------------------------------