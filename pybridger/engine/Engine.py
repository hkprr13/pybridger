#-------------------------------------------------------------------------------
from typing import Any
from .base      import MySqlEngine     
from .base      import Sqlite3Engine  
from .base      import PostgreSqlEngine 
from ..common   import public 
from ..common   import private
from ..schema   import Column
from ..model    import Model
from ..manager  import Select 
from ..config   import Config
from ..mapper   import Query
#-------------------------------------------------------------------------------
class Engine:
    """
    """
    #---------------------------------------------------------------------------
    def __init__(
            self,
            sqlEngineName : str,
            hostName      : str | None = None,
            userName      : str | None = None,
            password      : str | None = None,
            database      : str | None = None,
            port          : int | None = None,
            isAutoCreate  : bool       = False,
            logFile       : str | None = None
        ) -> None:
        """
        Initialize the engine and register the connection information
        Args:
            sqlEngineName (str) : SQL engine name
            hostName      (str) : host name
            userName      (str) : user name
            password      (str) : password
            databaseName  (str) : database name
        Examples:
            ```
            # Sqlite3
            engine = Engine(
                sqlEngineName = "sqlite3",
                database      = "database.db"
            )
            # MySQL
            engine = Engine(
                sqlEngineName = "MySQL",
                hostName      = "host",
                userName      = "user",
                password      = "password",
                database      = "database"
            )
            # PostgreSQL
            engine = Engine(
                sqlEngineName = "PostgreSQL",
                hostName      = "host",
                userName      = "user",
                password      = "password",
                database      = "database"
                port          = "3306"
            )
            ```
        """
        self.sqlEngineName  = sqlEngineName 
        self.hostName       = hostName
        self.userName       = userName
        self.password       = password
        self.database       = database
        self.port           = port
        self.logFile        = logFile
        self.__isAutoCreate = isAutoCreate
    #---------------------------------------------------------------------------
    @public
    def launch(self) -> None:
        """
        Initialize the SQL engine according to the engine name 
        Raises:
            ModuleNotFoundError : If an unsupported engine name is specified
        """
        if self.__isAutoCreate:
            Config.isAutoCreate = True
        if self.sqlEngineName.lower() == "sqlite3":
            if self.database:
                self.sqlEngine = Sqlite3Engine(
                    databasePath = self.database,
                    logFile      = self.logFile
                )
            else:
                raise Exception("Please specify the database")
        elif self.sqlEngineName.lower() == "mysql":
            if  self.hostName and self.userName \
            and self.password and self.database:
                self.sqlEngine = MySqlEngine(
                    hostName     = self.hostName,
                    userName     = self.userName,
                    password     = self.password,
                    databaseName = self.database,
                    logFile      = self.logFile
                )
            else:
                raise Exception("Please specify the argument")
        elif self.sqlEngineName.lower() == "postgresql":
            if  self.hostName and self.userName \
            and self.password and self.database \
            and self.port:
                self.sqlEngine = PostgreSqlEngine(
                    hostName     = self.hostName,
                    userName     = self.userName,
                    password     = self.password,
                    databaseName = self.database,
                    port         = self.port,
                    logFile      = self.logFile
                )
            else:
                raise Exception("Please specify the argument")
        else:
            raise ModuleNotFoundError("This is an unsupported module engine")
        Config.sqlEngine = self.sqlEngine
        Config.database  = self.database
    #---------------------------------------------------------------------------
    @public
    def commit(self) -> None:
        """
        Commit the transaction
        """
        self.sqlEngine.commit()
    #---------------------------------------------------------------------------
    @public
    def close(self) -> None:
        """
        close the transaction
        """
        self.sqlEngine.close()
    #---------------------------------------------------------------------------
    @public
    def select(
            self,
            table    : type[Model],
            *columns : Column
        ) -> Select:
        """
        Generate a Select object for the SELECT statement
        Args:
            table   (type[Model]) : Model class
            columns (Column...)   : Target columns for retrieval
        Returns:
            Select : Select object
        """
        return Select(
            tableName  = table.__tableName__,
            columns    = columns           
        )
    #---------------------------------------------------------------------------
    @public
    def get(
            self,
            *column : Column
        ) -> list[Any] | None:
        cols = list(column)
        firstTableClass : Column    = cols[0]
        firstTableName  : str       = firstTableClass.__tableName__
        foreignKeytables : list[str] = []
        tableColumnNames : list[str] = []
        for col in cols:
            tableName  = col.__tableName__
            columnName = col.__columnName__
            if not tableName in foreignKeytables \
            and not tableName == firstTableName:
                foreignKeytables.append(tableName)
            tableColumnName = f"{tableName}.{columnName}"
            if not tableColumnName in tableColumnNames:
                tableColumnNames.append(tableColumnName)
        innerJoinTables = self.__getInnerJoinTables(
            Config.models, foreignKeytables
        )
        query = self.__buildOneToOneQuery(
            selectColumns   = tableColumnNames,
            fromTable       = firstTableName,
            innerJoinTables = innerJoinTables,
            foreignKeys     = foreignKeytables
        )
        self.sqlEngine.execute(query)
        return self.sqlEngine.fetchall()
    #--------------------------------------------------------------------------
    @private
    def __getInnerJoinTables(
            self,
            models,
            foreignKeytables
        )-> list:
        innerJoinTables : list[str]   = []
        for fktable in foreignKeytables:
            for m in models:
                table = m[0]
                fks   = m[2]
                if table == fktable:
                    for fk in fks:
                        a = f"{table}.{fk[0]}"
                        b = f"{fk[1]}.{fk[2]}"
                        c = f"{a} = {b}"
                        innerJoinTables.append(c)
        return innerJoinTables
    #--------------------------------------------------------------------------
    @private
    def __buildOneToOneQuery(
            self,
            selectColumns   : list,
            fromTable       : str,
            innerJoinTables : list,
            foreignKeys     : list,
        )-> Query:
        selectColumn = ""
        for c in selectColumns:
            selectColumn += f"{c}, "
        selectColumn = selectColumn[:-2]
        innerJoinTable = ""
        for i in range(len(foreignKeys)):
            innerJoinTable += f"INNER JOIN {foreignKeys[i]} " \
                           +  f"ON {innerJoinTables[i]} "
        innerJoinTable = innerJoinTable[:-1] + ";"
        query = f"SELECT {selectColumn} FROM {fromTable} {innerJoinTable}"
        print(query)
        return Query(query)
#-------------------------------------------------------------------------------
