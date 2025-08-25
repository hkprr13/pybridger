#-------------------------------------------------------------------------------
from typing                     import Any
from .FloatingPointDataType     import FloatingPointDataType
from ....common                 import override
from ....common                 import private
from ....mapper                 import Query
#-------------------------------------------------------------------------------
class Float(FloatingPointDataType):
    """
    Define single precision floating point class.
    
    MySQL query      : "FLOAT(M, D) [UNSIGNED] [ZEROFILL]"
    Sqlite3 query    : "REAL"
    PostgreSQL query : "FLOAT(p)"
    """
    #---------------------------------------------------------------------------
    def __init__(
            self,
            M          : int,
            D          : int  | None = None,
            p          : int  | None = None,
            isUnsigned : bool        = False,
            isZeroFill : bool        = False
        ) -> None:
        """
        Initialize single precision floating point object
        Args:
            M          (int)  : decimal digits (supported sql MySQL)
            D          (int)  : scale          (supported sql MySQL)
            p          (int)  : binary precision (supported sql PostgreSQL)
            isUnsigned (bool) : Whether to enable UNSIGNED or not (supported sql MySQL)
            isZeroFill (bool) : Whether to enable ZEROFILL or not (supported sql MySQL)
        Examples:
            ```
            # Used MySQL
            dataType = FLoat(M = 2, D = 3)
            # Used Sqlite3
            dataType = Double()
            # Used PostgreSQL
            dataType = Float(p = 2)
            ```
        """
        super().__init__()
        self.M = M
        self.D = D
        self.p = p
        self.__isUnsigned = isUnsigned
        self.__isZeroFill = isZeroFill
    #---------------------------------------------------------------------------
    @private
    def __buildMySqlQuery(self) -> Query:
        """
        Build query by MySQL
        Returns:
            Query : query "FLOAT(M, D) [UNSIGNED] [ZEROFILL]"
        """
        query = f"FLOAT({self.M}"
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
            Query : query "FLOAT(p)"
        """
        query = f"FLOAT({self.p})"
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