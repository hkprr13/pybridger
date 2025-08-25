#-------------------------------------------------------------------------------
from typing                     import Any
from .FloatingPointDataType     import FloatingPointDataType
from ....common                 import override
from ....common                 import private
from ....mapper                 import Query
#-------------------------------------------------------------------------------
class Double(FloatingPointDataType):
    """
    Define double precision DOUBLEing point class.
    
    MySQL query      : "DOUBLE(M, D) [UNSIGNED] [ZEROFILL]"
    Sqlite3 query    : "REAL"
    PostgreSQL query : "DOUBLE(p)"
    """
    def __init__(
            self,
            M          : int,
            D          : int  | None = None,
            isUnsigned : bool        = False,
            isZeroFill : bool        = False
        ) -> None:
        """
        Initialize double precision DOUBLEing point object
        Args:
            M          (int)  : decimal digits (supported sql MySQL)
            D          (int)  : scale          (supported sql MySQL).
                                Specifying D is not recommended
            isUnsigned (bool) : Whether to enable UNSIGNED or not (supported sql MySQL)
            isZeroFill (bool) : Whether to enable ZEROFILL or not (supported sql MySQL)
        Examples:
            ```
            # Used MySQL
            dataType = Double(M = 2, D = 3)
            # Used Sqlite3
            dataType = Double()
            # Used PostgreSQL
            dataType = Double()
            ```
        """
        super().__init__()
        self.M = M
        self.D = D
        self.__isUnsigned = isUnsigned
        self.__isZeroFill = isZeroFill
    #---------------------------------------------------------------------------
    @private
    def __buildMySqlQuery(self) -> Query:
        """
        Build query by MySQL
        Returns:
            Query : query "DOUBLE(M, D) [UNSIGNED] [ZEROFILL]"
        """
        query = f"DOUBLE({self.M}"
        if self.D:
            query += f" ,{self.D})"
        else:
            query += f")"
        if self.__isUnsigned:
            query += " UNSIGNED"
        if self.__isZeroFill:
            query += " ZEROFILL"
        return Query(query)
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
            Query : query "DOUBLE PRECISION"
        """
        query = f"DOUBLE PRECISION"
        return Query(query)
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