#-------------------------------------------------------------------------------
from ...common      import private
from ...common      import public
from ...config      import Config
from ...schema      import Column
from ...mapper      import Query
from ...errors      import EngineUndefinedError
#-------------------------------------------------------------------------------
class Index:
    """
    Define Index class
    """
    def __init__(
            self,
            indexName : str,
            *columns  : Column
        ) -> None:
        """
        Initialize index object
        Args:
            indexName (str)    : Index name
            *columns  (Column) : Column object
        Examples:
            index = Index(“indexName”, User.id, User.name)
            # Create index
            index.create()
            # Drop index
            index.drop() # Each operation is automatically committed.
        """
        self.__indexName = indexName
        self.__columns   = columns
        self.__sqlEngine = Config.sqlEngine
    #---------------------------------------------------------------------------
    @ private
    def __columnsToSql(self) -> str:
        query = ""
        for col in self.__columns:
            if query == "":
                query += f"{col.tableName}("
            else:
                query += f"{col.columnName}, "
        else:
            query = query[:-2]
            query += ")"
        # User (id, name, ...)
        return query
    #---------------------------------------------------------------------------
    @ public
    def create(self) -> None:
        """
        Create index
        """
        # User (id, name, ...)
        colToSql = self.__columnsToSql()
        query = f"CREATE INDEX {self.__indexName} ON {colToSql};"
        if not self.__sqlEngine is None:
            self.__sqlEngine.execute(Query(query))
            self.__sqlEngine.commit()
        else:
            raise EngineUndefinedError()
    #---------------------------------------------------------------------------
    @ public
    def drop(self) -> None:
        """
        Delete Index
        """
        query = f"DROP INDEX IF NOT EXISTS {self.__indexName};"
        if not self.__sqlEngine is None:
            self.__sqlEngine.execute(Query(query))
            self.__sqlEngine.commit()
        else:
            raise EngineUndefinedError()
#-------------------------------------------------------------------------------