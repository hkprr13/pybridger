#-------------------------------------------------------------------------------
from typing import Any
from .ModelMeta    import ModelMeta
from ..config      import Config
from ..schema      import Column
from ..common      import private
from ..common      import public
from ..schema      import Constraint
from ..manager     import Base 
from ..manager     import AlterTableAddColumn
from ..manager     import AlterTableAddConstraint
from ..manager     import AlterTableDropColumn
from ..manager     import AlterTableDropConstraint
from ..manager     import AlterTableRenameColumn
from ..manager     import CreateIndex
from ..manager     import CreateTable
from ..manager     import CreateTableIfNotExists
from ..manager     import CreateTrigger
from ..manager     import CreateView
from ..manager     import InsertRecord
from ..manager     import InsertRecords
from ..manager     import Select
from ..manager     import UpdateRecord
from ..manager     import UpdateRecords
from ..manager     import DeleteRecord
from ..manager     import DropIndex
from ..manager     import DropIndexIfExists
from ..manager     import DropTable
from ..manager     import DropTableIfExists
from ..manager     import DropTrigger
from ..manager     import DropTriggerIfNotExists
from ..manager     import DropView
from ..manager     import DropViewIfExists
#-------------------------------------------------------------------------------
class Model(metaclass = ModelMeta):
    """
    Define Model class
    Attributes:
        tableName (str)                     : Automatically retrieved from class name
        columns   (list[dict[str, Column]]) : List of column definitions
    """
    tableName : str
    columns   : list[dict[str, Column]]
    __tableName__  : str 
    __relation__   : list
    __foreignKey__ : list
    __createSql__  : str
    #---------------------------------------------------------------------------
    @classmethod
    @private
    def __parameterColumnsToStrings(cls, columns :tuple[Column, ...]) -> str:
        cols = ""
        for col in columns:
            cols += col.columnName + ", "
        return cols[:-2]
    #---------------------------------------------------------------------------
    # @classmethod
    # @private
    # def __columnsToCreateQuery(cls) -> str:
    #     """
    #     Convert columns to query statements.
    #     Used when creating tables
    #     Returns:
    #         str : Create query
    #     """
    #     cls.__foreignKeyList = []
    #     columnDefineLists    = []
    #     # Add each column definition to the list
    #     for cols in cls.columns:
    #         columnQuery = cls.__columnsToQuery(cols)
    #         columnDefineLists.append(columnQuery)
    #     # If there is a foreign key, add it at the end
    #     for fk in cls.__foreignKeyList:
    #         columnDefineLists.append(fk)
    #     return ", ".join(columnDefineLists)
    # #---------------------------------------------------------------------------
    # @classmethod
    # @private
    # def __columnsToQuery(
    #         cls,
    #         columns : dict[str, Column]
    #     ) -> str:
    #     """
    #     Convert columns to a query statement.
    #     Private method used only in columnsToQuery
    #     Args:
    #         columns (dict[str, Column]) : Columns
    #     Returns:
    #         str : the query statement used in the Create statement
    #     """
    #     columnName, columnObject = next(iter(columns.items()))
    #     parts = []
    #     parts.append(columnName)
    #     if columnObject.dataTypeQuery.sql:
    #         parts.append(columnObject.dataTypeQuery.sql)
    #     if columnObject.primaryKeyQuery.sql:
    #         parts.append(columnObject.primaryKeyQuery.sql)
    #     if columnObject.autoIncrementQuery.sql:
    #         parts.append((columnObject.autoIncrementQuery.sql))
    #     if columnObject.defaultQuery.sql:
    #         parts.append(columnObject.defaultQuery.sql)
    #     if columnObject.uniqueQuery.sql:
    #         parts.append(columnObject.uniqueQuery.sql)
    #     if columnObject.notNullQuery.sql:
    #         parts.append(columnObject.notNullQuery.sql)
    #     # If defined, store separately
    #     fk = cls.__foreignKeyToQuery(columnName, columnObject)
    #     if fk:
    #         cls.__foreignKeyList.append(fk)        
    #     return " ".join(parts)
    # #---------------------------------------------------------------------------
    # @classmethod
    # @private
    # def __foreignKeyToQuery(
    #         cls,
    #         columnName : str,
    #         columnObject : Column
    #     ) -> str:
    #     """
    #     Private method that outputs foreign key constraints as a query statement
    #     Args:
    #         columnName   (str) : Column name.
    #         cokumnObject (str) : Column object.
    #     Returns:
    #         fk : Query statement.
    #     """
    #     fk = columnObject.foreignKeyQuery.sql
    #     if fk:
    #         fk = fk.replace("~~~", columnName)
    #     else:
    #         fk = ""
    #     return fk
    # #---------------------------------------------------------------------------
    # @classmethod
    # def checkDatatypes(cls) -> None:
    #     print(cls.__dict__)
    # #---------------------------------------------------------------------------
    # @classmethod
    # @public
    # def createTable(cls) -> CreateTable:
    #     """
    #     Create a table
    #     Returns:
    #         CreateTable : Table creation object
    #     Exemples:
    #         ```
    #         user = User.createTable()
    #         user.execute()
    #         user.commit()
    #         ```
    #     """
    #     columns = cls.__columnsToCreateQuery()
    #     return CreateTable(
    #         tableName = cls.tableName,
    #         columns   = columns
    #     )
    # #---------------------------------------------------------------------------
    # @classmethod
    # @public
    # def createTableIfNotExists(cls) -> CreateTableIfNotExists:
    #     """
    #     Create a table if it does not exist
    #     Returns:
    #         CreateTableIfNotExists : Table creation object
    #     Exemples:
    #         ```
    #         user = User.createTableIfNotExists()
    #         user.execute()
    #         user.commit()
    #         ```
    #     """
    #     columns = cls.__columnsToCreateQuery()
    #     return CreateTableIfNotExists(
    #         tableName = cls.tableName,
    #         columns   = columns
    #     )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    def createIndex(
            cls,
            indexName : str,
            *columns  : Column
        ) -> CreateIndex:
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
        return CreateIndex(
            indexName = indexName,
            tableName = cls.tableName,
            columns   = cols
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    def createView(cls): ...
    #---------------------------------------------------------------------------
    @classmethod
    @public
    def createTrigger(
            cls,
            triggerName : str,
            timing      : str,
            event       : str,
            body        : Base
        ) -> CreateTrigger:
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
        return CreateTrigger(
            tableName   = cls.tableName, 
            triggerName = triggerName,
            timing      = timing,
            event       = event,
            body        = body.query
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    def dropTable(cls) -> DropTable:
        """
        Delete a table
        Examples:
            ```
            user = User.dropTable()
            user.execute()
            user.commit()
            ```
        Returns:
            DropTable : Table deletion object
        """
        return DropTable(
            tableName = cls.tableName
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    def dropTableIfExists(cls) -> DropTableIfExists:
        """
        Delete only if the table exists
        Example:
            ```
            user = User.dropTableIfExists()
            user.execute()
            user.commit()
            ```
        Returns:
            DropTableIfExists : Table deletion object
        """
        return DropTableIfExists(
            tableName = cls.tableName
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    def dropView(cls, viewName : str) -> DropView:
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
            DropView : View deletion object
        """
        return DropView(
            tableName = cls.tableName,
            viewName  = viewName
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    def dropViewIfExist(cls, viewName : str) -> DropViewIfExists:
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
            DropViewIfExists : View deletion object
        """
        return DropViewIfExists(
            tableName = cls.tableName,
            viewName  = viewName
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    def dropIndex(cls, indexName : str) -> DropIndex:
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
            DropIndex : Index deletion object
        """
        return DropIndex(
            tableName = cls.tableName,
            indexName = indexName
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    def dropIndexIfNotExists(cls, indexName : str) -> DropIndexIfExists:
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
            DropIndexIfExists : Index deletion object
        """
        return DropIndexIfExists(
            tableName = cls.tableName,
            indexName = indexName
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    def dropTrigger(cls, triggerName : str) -> DropTrigger:
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
            DropTrigger : Trigger deletion object
        """
        return DropTrigger(
            tableName   = cls.tableName,
            triggerName = triggerName
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    def dropTriggerIfNotExists(
            cls,
            triggerName : str
        ) -> DropTriggerIfNotExists:
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
            DropTriggerIfNotExists : Trigger deletion object
        """
        return DropTriggerIfNotExists(
            tableName   = cls.tableName,
            triggerName = triggerName
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    def insertRecord(cls, **columns) -> InsertRecord:
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
            InsertRecord : Returns the record insertion object
        """
        cols         = ""
        placeHolders = ""
        values       = []
        for key, value in columns.items():
            Model()
            cols         += f"{key}, "
            placeHolders += "?, "
            values.append(value)
        return InsertRecord(
            tableName    = cls.tableName,
            columns      = cols[:-2],
            values       = tuple(values),
            placeHolders = placeHolders[:-2]
        )
    #---------------------------------------------------------------------------
    @classmethod    
    @public
    def insertRecords(cls, **columns) -> InsertRecords:
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
        return InsertRecords(
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
    def updateRecord(cls, **updateColumns) -> UpdateRecord:
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
        return UpdateRecord(
            tableName    = cls.tableName,
            columns      = cols[:-2] + " ", # Insert a space before WHERE
            values       = tuple(values),
        )
    #---------------------------------------------------------------------------
    @classmethod    
    @public
    def updateRecords(cls, **updateColumns) -> UpdateRecords:
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
        return UpdateRecords(
            tableName = cls.tableName,
            columns   = cols[:-2] + " ", # Insert a space before WHERE
            data      = list(zip(*updateColumns.values()))
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    def deleteRecord(cls, **deleteColumns) -> DeleteRecord:
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
        return DeleteRecord(
            tableName = cls.tableName,
            columns   = cols[:-2] + " ", # Insert a space before WHERE
            values    = tuple(values)
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    def alterTableAddColumn(cls, **column : Column) -> AlterTableAddColumn:
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
            AlterTableAddColumn : Column addition object
        """
        columnName   : str    # カラム名
        columnObject : Column # カラムオブジェクト
        # カラム
        for key, value in column.items():
            columnName   = key
            columnObject = value
        # 条件
        constraints = f"{columnObject.notNullQuery.sql} "\
                    + f"{columnObject.notNullQuery.sql} "\
                    + f"{columnObject.uniqueQuery.sql}"
        return AlterTableAddColumn(
            tableName   = cls.tableName,
            column      = columnName,
            dataType    = columnObject.dataTypeQuery.sql,
            constraints = constraints
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    def alterTableDropColumn(
            cls,
            column : Column
        ) -> AlterTableDropColumn:
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
            AlterTableDropColumn : Column deletion object
        """
        return AlterTableDropColumn(
            tableName  = cls.tableName,
            columnName = column.columnName
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    def alterTableRenameColumn(
            cls,
            oldName : str,
            newName : str
        ) -> AlterTableRenameColumn:
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
            AlterTableRenameColumn : Column name change object
        """
        return AlterTableRenameColumn(
            tableName = cls.tableName,
            oldName   = oldName,
            newName   = newName
        )
    #---------------------------------------------------------------------------
    @classmethod
    @public
    def alterTableAddConstraint(cls,**constraints : Constraint): ...
    #---------------------------------------------------------------------------
    @classmethod
    @public
    def alterTableDropConstraint(cls): ...
    #---------------------------------------------------------------------------
    @classmethod
    @public
    def alterView(cls): ...
    #---------------------------------------------------------------------------
    @classmethod
    @public
    def fromDict(cls, data : dict):
        instance = cls()
        for key, value in data.items():
            if hasattr(isinstance, key):
                setattr(instance, key, value)
        return instance
    #---------------------------------------------------------------------------
    def __and__(self, other) -> str:
        return f"{self} {other}"
#-------------------------------------------------------------------------------