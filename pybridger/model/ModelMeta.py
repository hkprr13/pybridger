#-------------------------------------------------------------------------------
from typing         import ClassVar
from ..mapper       import Query
from ..schema       import Column
from ..schema       import Field
from ..config       import Config
#-------------------------------------------------------------------------------
class ModelMeta(type):
    """
    Define model meta class
    """
    def __new__(mcs, name, bases, namespace):
        """
        Definition immediately before being called
        Args:
            mcs       (_type_) : self or cls
            name      (_type_) : model name 
            bases     (_type_) : ?
            namespace (_type_) : attributes

        Raises:
            Exception: _description_

        Returns:
            _type_: _description_
        """
        # The model itself does not require columns.
        if name == "Model":
            return super().__new__(mcs, name, bases, namespace)
        columns    = []
        referenced = []
        colDefs    = []
        constrains = []
        createSql  = f"CREATE TABLE IF NOT EXISTS {name} ("
        for columnName, column in namespace.items():
            # Column class or field class
            if isinstance(column, Column) \
            or isinstance(column, Field):
                # Build create table sql
                column.tableName  = name
                column.columnName = columnName
                colDefs.append(" ".join(column.buildCreateList()))
                fkQuery           = column.buildForeignKeyQuery()
                if fkQuery.sql:
                    constrains.append(fkQuery.sql)
                tblCheckQuery = column.buildTableLevelCheckQuery()
                if tblCheckQuery.sql:
                    constrains.append(tblCheckQuery.sql) 
                # Referenced
                if column.referencedTable: 
                    referenced.append(
                        (column.referencedTable, column.referencedColumn)
                    )
                columns.append({columnName : column}) # Save in dictionary format
    
        createSql += ", ".join(colDefs + constrains) +");"
        # Exception if there are no columns
        if not columns:
            raise Exception(f"[{name}] No columns are defined in the class.")
        # Add table name and column list as class attributes
        namespace["tableName"]      = name
        namespace["columns"]        = columns
        namespace["__relations__"]  = []
        if referenced:
            namespace["__foreignKey__"] = referenced
        else:
            namespace["__foreignKey__"] = []
        # If auto creation is enabled, create the table
        if Config.isAutoCreate:
            engine = Config.sqlEngine
            if engine:
                engine.execute(Query(createSql))
                engine.commit()
        return super().__new__(mcs, name, bases, namespace)
    #-------------------------------------------------------------------------------
