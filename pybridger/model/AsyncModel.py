#-------------------------------------------------------------------------------
from .ModelMeta     import ModelMeta
from ..schema       import Column
from ..common       import private
from ..common       import public
from ..schema       import Constraint
from ..manager      import Base 
from ..manager      import AsyncAlterTableAddColumn
from ..manager      import AsyncAlterTableAddConstraint
from ..manager      import AsyncAlterTableDropColumn
from ..manager      import AsyncAlterTableDropConstraint
from ..manager      import AsyncAlterTableRenameColumn
from ..manager      import AsyncCreateIndex
from ..manager      import AsyncCreateTable
from ..manager      import AsyncCreateTableIfNotExists
from ..manager      import AsyncCreateTrigger
from ..manager      import AsyncCreateView
from ..manager      import AsyncInsertRecord
from ..manager      import AsyncInsertRecords
from ..manager      import AsyncUpdateRecord
from ..manager      import AsyncUpdateRecords
from ..manager      import AsyncDeleteRecord
from ..manager      import AsyncDropIndex
from ..manager      import AsyncDropIndexIfExists
from ..manager      import AsyncDropTable
from ..manager      import AsyncDropTableIfExists
from ..manager      import AsyncDropTrigger
from ..manager      import AsyncDropTriggerIfNotExists
from ..manager      import AsyncDropView
from ..manager      import AsyncDropViewIfExists
from ..manager      import Select
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
class Model(metaclass = ModelMeta):
    """
    Define Model class
    Attributes:
        tableName (str)                     : Automatically retrieved from class name
        columns   (list[dict[str, Column]]) : List of column async definitions
    """
    tableName : str
    columns   : list[dict[str, Column]]
    #---------------------------------------------------------------------------
    @classmethod
    @private
    def __parameterColumnsToStrings(cls, columns :tuple[Column, ...]) -> str:
        cols = ""
        for col in columns:
            cols += col.columnName + ", "
        return cols[:-2]
    #---------------------------------------------------------------------------
    @classmethod
    @private
    def __columnsToCreateQuery(cls) -> str:
        """
        Convert columns to query statements.
        Used when creating tables
        Returns:
            str : Create query
        """
        cls.__foreignKeyList = []
        columnDefineLists    = []
        # Add each column async definition to the list
        for cols in cls.columns:
            columnQuery = cls.__columnsToQuery(cols)
            columnDefineLists.append(columnQuery)
        # If there is a foreign key, add it at the end
        for fk in cls.__foreignKeyList:
            columnDefineLists.append(fk)
        return ", ".join(columnDefineLists)
    #---------------------------------------------------------------------------
    @classmethod
    @private
    async def __columnsToQuery(
            cls,
            columns : dict[str, Column]
        ) -> str:
        """
        Convert columns to a query statement.
        Private method used only in columnsToQuery
        Args:
            columns (dict[str, Column]) : Columns
        Returns:
            str : the query statement used in the Create statement
        """
        columnName, columnObject = next(iter(columns.items()))
        parts = []
        parts.append(columnName)
        if columnObject.dataTypeQuery.sql:
            parts.append(columnObject.dataTypeQuery.sql)
        if columnObject.primaryKeyQuery.sql:
            parts.append(columnObject.primaryKeyQuery.sql)
        if columnObject.autoIncrementQuery.sql:
            parts.append((columnObject.autoIncrementQuery.sql))
        if columnObject.defaultQuery.sql:
            parts.append(columnObject.defaultQuery.sql)
        if columnObject.uniqueQuery.sql:
            parts.append(columnObject.uniqueQuery.sql)
        if columnObject.notNullQuery.sql:
            parts.append(columnObject.notNullQuery.sql)
        # If async defined, store separately
        fk = cls.__foreignKeyToQuery(columnName, columnObject)
        if fk:
            cls.__foreignKeyList.append(fk)        
        return " ".join(parts)
    #---------------------------------------------------------------------------
    @classmethod
    @private
    async def __foreignKeyToQuery(
            cls,
            columnName : str,
            columnObject : Column
        ) -> str:
        """
        Private method that outputs foreign key constraints as a query statement
        Args:
            columnName   (str) : Column name.
            cokumnObject (str) : Column object.
        Returns:
            fk : Query statement.
        """
        fk = columnObject.foreignKeyQuery.sql
        if fk:
            fk = fk.replace("~~~", columnName)
        else:
            fk = ""
        return fk
    #---------------------------------------------------------------------------
    @classmethod
    async def checkDatatypes(cls) -> None:
        print(cls.__dict__)
    #---------------------------------------------------------------------------
    @classmethod
    @public
    async def createTable(cls) -> AsyncCreateTable:
        """
        Create a table
        Returns:
            CreateTable : Table creation object
        Exemples:
            ```
            user = User.createTable()
            user.execute()
            user.commit()
            ```
        """
        columns = cls.__columnsToCreateQuery()
        return AsyncCreateTable(
            tableName = cls.tableName,
            columns   = columns
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    async def createTableIfNotExists(cls) -> AsyncCreateTableIfNotExists:
        """
        Create a table if it does not exist
        Returns:
            CreateTableIfNotExists : Table creation object
        Exemples:
            ```
            user = User.createTableIfNotExists()
            user.execute()
            user.commit()
            ```
        """
        columns = cls.__columnsToCreateQuery()
        return AsyncCreateTableIfNotExists(
            tableName = cls.tableName,
            columns   = columns
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    async def createIndex(
            cls,
            indexName : str,
            *columns  : Column
        ) -> AsyncCreateIndex:
        """
        Create an index
        Args:
            indexName (str)    : Name of the index to be created
            *columns  (Column) : Target columns
        Returns:
            CreateIndex : Index creation processing object
        Examples:
            ```
            user = User.createIndex("indexName", User.id, User.name)
            user.execute()
            user.commit()
            ```
        """
        cols = cls.__parameterColumnsToStrings(columns)
        return AsyncCreateIndex(
            indexName = indexName,
            tableName = cls.tableName,
            columns   = cols
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    async def createView(cls): ...
    #---------------------------------------------------------------------------
    @classmethod
    @public
    async def createTrigger(
            cls,
            triggerName : str,
            timing      : str,
            event       : str,
            body        : Base
        ) -> AsyncCreateTrigger:
        """
        Creating a trigger
        Args:
            triggerName (str) : Trigger name 
            timing      (str) : Timing BEFORE or AFTER
            event       (str) : Event  INSERT or UPDATE or DELETE
            body        (str) : Query statement to execute
        Examples:
            ```
            trigger = User.createTrigger(
                "tableName,
                "triggerName",
                "before | after",
                "insert | update | delete",
                User.InsertRecord() <-Enter the query you want to execute
            )
            trigger.execute()
            trigger.commit()
            ```
        """
        return AsyncCreateTrigger(
            tableName   = cls.tableName, 
            triggerName = triggerName,
            timing      = timing,
            event       = event,
            body        = body.query
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    async def dropTable(cls) -> AsyncDropTable:
        """
        Delete a table
        Examples:
            ```
            user = User.dropTable()
            user.execute()
            user.commit()
            ```
        Returns:
            AsyncDropTable : Table deletion object
        """
        return AsyncDropTable(
            tableName = cls.tableName
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    async def dropTableIfExists(cls) -> AsyncDropTableIfExists:
        """
        Delete only if the table exists
        Example:
            ```
            user = User.dropTableIfExists()
            user.execute()
            user.commit()
            ```
        Returns:
            AsyncDropTableIfExists : Table deletion object
        """
        return AsyncDropTableIfExists(
            tableName = cls.tableName
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    async def dropView(cls, viewName : str) -> AsyncDropView:
        """
        Deleting a view
        Args:
            viewName (str) : Name of the view to be deleted
        Example:
            ```
            user = User.dropView("view")
            user.execute()
            user.commit()
            ```
        Returns:
            AsyncDropView : View deletion object
        """
        return AsyncDropView(
            tableName = cls.tableName,
            viewName  = viewName
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    async def dropViewIfExist(cls, viewName : str) -> AsyncDropViewIfExists:
        """
        Delete a view if it exists
        Args:
            viewName (str) : Name of the view to delete
        Example:
            ```
            user = User.dropView("view")
            user.execute()
            user.commit()
            ```
        Returns:
            AsyncDropViewIfExists : View deletion object
        """
        return AsyncDropViewIfExists(
            tableName = cls.tableName,
            viewName  = viewName
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    async def dropIndex(cls, indexName : str) -> AsyncDropIndex:
        """
        Index deletion
        Args:
            indexName (str) : Index name
        Example:
            ```
            user = User.dropIndex("index")
            user.execute()
            user.commit()
            ```
        Returns:
            AsyncDropIndex : Index deletion object
        """
        return AsyncDropIndex(
            tableName = cls.tableName,
            indexName = indexName
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    async def dropIndexIfNotExists(cls, indexName : str) -> AsyncDropIndexIfExists:
        """
        Index deletion
        Args:
            indexName (str) : Index name
        Example:
            ```
            user = User.dropIndexIfExists("index")
            user.execute()
            user.commit()
            ```
        Returns:
            AsyncDropIndexIfExists : Index deletion object
        """
        return AsyncDropIndexIfExists(
            tableName = cls.tableName,
            indexName = indexName
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    async def dropTrigger(cls, triggerName : str) -> AsyncDropTrigger:
        """
        Deleting a trigger
        Args:
            triggerName (str) : Trigger name
        Examples:
            ```
            user = User.dropTrigger("trigger")
            user.execute()
            user.commit()
            ```
        Returns:
            AsyncDropTrigger : Trigger deletion object
        """
        return AsyncDropTrigger(
            tableName   = cls.tableName,
            triggerName = triggerName
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    async def dropTriggerIfNotExists(
            cls,
            triggerName : str
        ) -> AsyncDropTriggerIfNotExists:
        """
        Deleting a trigger
        Args:
            triggerName (str) : Trigger name
        Examples:
            ```
            user = User.dropTriggerIfNotExists("trigger")
            user.execute()
            user.commit()
            ```
        Returns:
            AsyncDropTriggerIfNotExists : Trigger deletion object
        """
        return AsyncDropTriggerIfNotExists(
            tableName   = cls.tableName,
            triggerName = triggerName
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    async def insertRecord(cls, **columns) -> AsyncInsertRecord:
        """
        Insert record
        Args:
            columns : Example: id = 1, name = "name", age = 19...
        Examples:
            ```
            user = User.insertRecord(id = 1, name = "name", age = 19)
            user.execute()
            user.commit()
            # A record with id = 1, name = "name", and age = 19
            # is inserted into the User table
            ```
        Returns:
            AsyncInsertRecord : Returns the record insertion object
        """
        cols         = ""
        placeHolders = ""
        values       = []
        for key, value in columns.items():
            Model()
            cols         += f"{key}, "
            placeHolders += "?, "
            values.append(value)
        return AsyncInsertRecord(
            tableName    = cls.tableName,
            columns      = cols[:-2],
            values       = tuple(values),
            placeHolders = placeHolders[:-2]
        )
    #---------------------------------------------------------------------------
    @classmethod    
    @public
    async def insertRecords(cls, **columns) ->AsyncInsertRecords:
        """
        Insert multiple records
        Arguments:
            **columns : Ex(id = [1, 2, 3], name = ["a", "b", "c"], age  = [19, 22, 17])
        Example:
            ```
            user = User.insertRecord(
                id   = [  1,   2,   3],
                name = ["a", "b", "c"],
                age  = [ 19,  22,  17]
            )
            user.execute()
            user.commit()
            # Multiple records are inserted into the User table:
            # |id|name|user|
            # |1 |a   |19  |
            # |2 |b   |22  |
            # |3 |c   |17  |
            ```
        Return value:
            InsertRecord: Returns a object for inserting multiple records
        """
        cols         = ""
        placeHolders = ""
        for key, values in columns.items():
            cols         += f"{key}, "
            placeHolders += "?, "
        return AsyncInsertRecords(
            tableName    = cls.tableName,
            columns      = cols[:-2],        # Pass in the form of id, name,
            data         = list(             # ... and delete the suffix
                zip(*columns.values())       
            ), 
            placeHolders = placeHolders[:-2] # Placeholder, delete the end         
        )
    #---------------------------------------------------------------------------
    @classmethod    
    @public
    async def updateRecord(cls, **updateColumns) -> AsyncUpdateRecord:
        """
        Update record
        Args:
            **updateColumns : Specify the columns to be updated.
        Examples:
            ```
            user = User.updateRecord(name = "a", age = 20)
            user.where(id = 1)
            user.execute()
            user.commit()
            ```
        Returns:
            UpdateRecord : Returns the record update object
        """
        cols   = ""
        values = []
        # Formatted as id = ?, name = ?, age = ?
        for key, value in updateColumns.items():
            cols += f"{key} = ?, "
            values.append(value)
        return AsyncUpdateRecord(
            tableName    = cls.tableName,
            columns      = cols[:-2] + " ", # Insert a space before WHERE
            values       = tuple(values),
        )
    #---------------------------------------------------------------------------
    @classmethod    
    @public
    async def updateRecords(cls, **updateColumns) -> AsyncUpdateRecords:
        """
        Update records
        Args:
            **updateColumns : Specify the columns to be updated
        Examples:
            ```
            user = User.updateRecords(
                name = ["a","b","c"], age = [20,22,24]
            ).where(id = [1,2,3]) # Don't forget to include where
            user.execute()
            user.commit()
            ```
        Returns:
            UpdateRecords : Returns a multiple record update object
        """
        cols = ""
        for key, value in updateColumns.items():
            cols += f"{key} = ?, "
        return AsyncUpdateRecords(
            tableName = cls.tableName,
            columns   = cols[:-2] + " ", # Insert a space before WHERE
            data      = list(zip(*updateColumns.values()))
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    async def deleteRecord(cls, **deleteColumns) -> AsyncDeleteRecord:
        """
        Delete a record
        Args:
            **deleteColumns : Specify the columns to be deleted
        Examples:
            ```
            user = User.deleteRecord(id = 1) # Multiple specifications are not allowed
            user.execute()
            user.commit()
            ```
        Returns:
            DeleteRecord : Returns a record deletion object
        """
        cols    = ""
        values = []
        # Formed into the shape of id = ?
        for key, value in deleteColumns.items():
            cols += f"{key} = ?, "
            values.append(value)
        return AsyncDeleteRecord(
            tableName = cls.tableName,
            columns   = cols[:-2] + " ", # Insert a space before WHERE
            values    = tuple(values)
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    async def alterTableAddColumn(cls, **column : Column) -> AsyncAlterTableAddColumn:
        """
        Add a column to a table
        Args:
            column (Column) : Column
        Examples:
            ```
            user = User.alterTableAddColumn(age = Column(Integer()))
            user.execute()
            user.commit()
            ```
        Returns:
            AsyncAlterTableAddColumn : Column addition object
        """
        columnName   : str 
        columnObject : Column 
        # カラム
        for key, value in column.items():
            columnName   = key
            columnObject = value
        # 条件
        constraints = f"{columnObject.notNullQuery.sql} "\
                    + f"{columnObject.notNullQuery.sql} "\
                    + f"{columnObject.uniqueQuery.sql}"
        return AsyncAlterTableAddColumn(
            tableName   = cls.tableName,
            column      = columnName,
            dataType    = columnObject.dataTypeQuery.sql,
            constraints = constraints
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    async def alterTableDropColumn(
            cls,
            column : Column
        ) -> AsyncAlterTableDropColumn:
        """
        Delete a column from a table
        Args:
            column (Column) : Column
        Examples:
            ```
            user = User.alterTableDropColumn(User.age)
            user.execute()
            user.commit()
            ```
        Returns:
            AsyncAlterTableDropColumn : Column deletion object
        """
        return AsyncAlterTableDropColumn(
            tableName  = cls.tableName,
            columnName = column.columnName
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    async def alterTableRenameColumn(
            cls,
            oldName : str,
            newName : str
        ) -> AsyncAlterTableRenameColumn:
        """
        Change table column name
        Args:
            oldName (str) : Existing name 
            newName (str) : New name
        Examples:
            ```
            user = User.alterTableRenameColumn("email", "address")
            user.execute()
            user.commit()
            ```
        Returns:
            AsyncAlterTableRenameColumn : Column name change object
        """
        return AsyncAlterTableRenameColumn(
            tableName = cls.tableName,
            oldName   = oldName,
            newName   = newName
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    async def alterTableAddConstraint(cls,**constraints : Constraint): ...
    #---------------------------------------------------------------------------
    @classmethod
    @public
    async def alterTableDropConstraint(cls): ...
    #---------------------------------------------------------------------------
    @classmethod
    @public
    async def alterView(cls): ...
    #---------------------------------------------------------------------------
    @classmethod
    @public
    async def fromDict(cls, data : dict):
        instance = cls()
        for key, value in data.items():
            if hasattr(isinstance, key):
                setattr(instance, key, value)
        return instance
    #---------------------------------------------------------------------------
    async def __and__(self, other) -> str:
        return f"{self} {other}"
#-------------------------------------------------------------------------------