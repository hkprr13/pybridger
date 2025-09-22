#-------------------------------------------------------------------------------
from __future__ import annotations # To avoid circular imports
from typing import TYPE_CHECKING 
#-------------------------------------------------------------------------------
if TYPE_CHECKING:
    from ..engine import Sqlite3Engine
    from ..engine import AsyncSqlite3Engine
    from ..engine import MySqlEngine
    from ..engine import AsyncMySqlEngine
    from ..engine import PostgreSqlEngine
    from ..engine import AsyncPostgreSqlEngine
#-------------------------------------------------------------------------------
class Config:
    """
    Defined config class
    Attributes:
        sqlEngine      (Sqlite3Engine      | MySqlEngine      | PostgreSqlEngine      | None) : Initial value None
        asyncSqlEngine (AsyncSqlite3Engine | AsyncMySqlEngine | AsyncPostgreSqlEngine | None) : Initial value None
        database       (str | None) : database
        sqlite3Engine         (Sqlite3Engine)         : Sqlite3
        mySqlEngine           (MySqlEngine)           : MySQL
        postgreSqlEngine      (PostgreSqlEngine)      : PostgreSQL
        asyncSqlite3Engine    (AsyncSqlite3Engine)    : Sqlite3(Asynchronous)
        asyncMySqlEngine      (AsyncMySqlEngine)      : MySQL(Asynchronous)
        asyncPostgreSqlEngine (AsyncPostgreSqlEngine) : PostgreSQL(Asynchronous)
    """
    # Synchronous engine
    sqlEngine : Sqlite3Engine    \
              | MySqlEngine      \
              | PostgreSqlEngine \
              | None = None
    # Asynchronous engine
    asyncSqlEngine : AsyncSqlite3Engine    \
                   | AsyncMySqlEngine      \
                   | AsyncPostgreSqlEngine \
                   | None = None
    # Database
    database : str | None = None
    # Auto create Table
    isAutoCreate : bool = False
    # models = [[table, ["id", "name"], ["User", "o-<", "Post"]], ...]
    models : list = []
    # modelClasses = [object1, object2]
    modelClasses : list = []
    @classmethod
    def appendModelClasses(cls, table):
        lst = cls.modelClasses
        if not table in lst:
            lst.append(table)
#-------------------------------------------------------------------------------