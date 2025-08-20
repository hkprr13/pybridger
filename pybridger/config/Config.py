#-------------------------------------------------------------------------------
from __future__ import annotations # 循環インポートを回避する用
from typing import TYPE_CHECKING   
#-------------------------------------------------------------------------------
if TYPE_CHECKING:
    from ..engine import Sqlite3Engine          # 
    from ..engine import AsyncSqlite3Engine     #
    from ..engine import MySqlEngine            #
    from ..engine import AsyncMySqlEngine       #
    from ..engine import PostgreSqlEngine       #
    from ..engine import AsyncPostgreSqlEngine  #
#-------------------------------------------------------------------------------
class Config:
    # 同期版のエンジン
    sqlEngine : Sqlite3Engine    \
              | MySqlEngine      \
              | PostgreSqlEngine \
              | None = None
    # 非同期版のエンジン
    asyncSqlEngine : AsyncSqlite3Engine    \
                   | AsyncMySqlEngine      \
                   | AsyncPostgreSqlEngine \
                   | None = None
    # データベース
    database : str | None = None
    # 比較用
    sqlite3Engine           : Sqlite3Engine
    mySqlEngine             : MySqlEngine
    postgreSqlEngine        : PostgreSqlEngine
    asyncSqlite3Engine      : AsyncSqlite3Engine
    asyncMySqlEngine        : AsyncMySqlEngine
    asyncPostgreSqlEngine   : AsyncPostgreSqlEngine
#-------------------------------------------------------------------------------