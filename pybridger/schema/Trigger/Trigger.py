#-------------------------------------------------------------------------------
from typing import Any
from ...engine      import MySqlEngine
from ...engine      import Sqlite3Engine
from ...engine      import PostgreSqlEngine
from ...common      import private
from ...common      import public
from ...config      import Config
from ...mapper      import Query
from ...errors      import EngineUndefinedError
from ...errors      import EngineUnsupportedError
#-------------------------------------------------------------------------------
class Trigger:
    """
    Define trigger class
    """
    def  __init__(
            self,
            triggerName : str,
            tableName   : str
        ) -> None:
        """
        Create a trigger on the table. No output
        Args:
            triggerName (str) : Trigger name
            tableName   (str) : Table name
        Examples:
            ‘’'
            trigger = Trigger(
                triggerName = “triggerName”,
                tableName   = “tableName”
            )
            ```
        """
        self.__triggerName = triggerName
        self.__tableName   = tableName
    #---------------------------------------------------------------------------
    @property
    @private
    def __sqlEngine(self) -> Sqlite3Engine | MySqlEngine | PostgreSqlEngine:
        engine = Config.sqlEngine
        if engine is None:
            raise EngineUndefinedError()
        return engine
    #---------------------------------------------------------------------------
    @private
    def __buildCreateQuery(
            self,
            timing : str,
            event  : str,
            body   : str
        ) -> Query:
        """
        Args:
            timing (str) : Timing
            event  (str) : Event  
            body   (str) : SQL statement to execute
        Raises:
            ValueError : When specifying an invalid argument
        Returns:
            Query : Query class
        """
        timingUpper : str = timing.upper()
        eventUpper  : str = timing.upper()
        if not timingUpper in ("BEFORE", "AFTER"):
            raise ValueError(f"Specified an invalid argument ({timing})")
        if not eventUpper in ("INSERT", "UPDATE", "DELETE"):
            raise ValueError(f"Specified an invalid argument ({event})")
        query = Query(
            f"CREATE TRIGGER {self.__triggerName} "
            f"{timingUpper} {eventUpper} ON {self.__tableName}"
            f"FOR EACH ROW BEGIN {body} END;"
        )
        return query
    #---------------------------------------------------------------------------
    @property
    @private
    def __buildShowQuery(self) -> Query:
        """
        Show query
        Raises:
            EngineUnsupportedError : Unsupported error
        """
        if self.__sqlEngine == Config.mySqlEngine:
            query = "SHOW TRIGGERS;"
        elif self.__sqlEngine == Config.sqlite3Engine:
            query = "SELECT name, tbl_name, sql "\
                  + "FROM sqlite_master WHERE type='trigger';"
        else:
            raise EngineUnsupportedError()
        return Query(query)
    #---------------------------------------------------------------------------
    @property
    @private
    def __buildDropQuery(self) -> Query:
        """
        Delete query
        """
        return Query(f"DROP TRIGGER IF EXISTS {self.__triggerName}")
    #---------------------------------------------------------------------------
    @public
    def create(
            self,
            timing : str,
            event  : str,
            body   : str
        ) -> None:
        """
        Create trigger
        Args:
            timing (str) : Timing BEFORE AFTER
            event  (str) : Event  INSERT UPDATE DELETE
            body   (str) : SQL statement to execute
        Examples:
            ```
            trigger = Trigger("triggerName", "tableName")
            trigger.create(
                "before | after", "insert | update | delete", "SQL statement"
            )
            ```
        """
        self.__sqlEngine.execute(
            self.__buildCreateQuery(timing, event, body)
        )
    #---------------------------------------------------------------------------
    @public
    def show(self) -> list[Any] | None: 
        """
        Show trigger
        """
        self.__sqlEngine.execute(self.__buildShowQuery)
        return self.__sqlEngine.fetchall()
    #---------------------------------------------------------------------------
    def drop(self) -> None: 
        """
        Delete trigger
        """
        self.__sqlEngine.execute(self.__buildDropQuery)
#-------------------------------------------------------------------------------