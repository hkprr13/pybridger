#-------------------------------------------------------------------------------
from ..schema   import Column
from ..schema   import Field
from ..config   import Config
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
class ModelMeta(type):
    """
    """
    def __new__(mcs, name, bases, namespace):
        # The model itself does not require columns.
        if name == "Model":
            return super().__new__(mcs, name, bases, namespace)
        columns    = []
        referenced = []
        createSql  = []
        for key, value in namespace.items():
            # Column class or field class
            if isinstance(value, Column) or isinstance(value, Field):
                value.columnName = key       # Set attribute names for column names
                value.tableName  = name      # Set the class name for the table name
                createSql.append(value.buildCreateQuery().sql)
                # If it has an attribute with value referencedTable
                if hasattr(value, "referencedTable"):
                    referencedTable  = value.referencedTable
                    referencedColumn = value.referencedColumn
                    referenced.append((referencedTable, referencedColumn))
                columns.append({key: value}) # Save in dictionary format
        # Exception if there are no columns
        if not columns:
            raise Exception(f"[{name}] No columns are defined in the class.")
        # Add table name and column list as class attributes
        namespace["tableName"]      = name
        namespace["columns"]        = columns
        namespace["__relation__"]   = []
        namespace["__foreignKey__"] = []
        if referenced:
            namespace["__foreignKey__"] = referenced
        print(createSql)
        return super().__new__(mcs, name, bases, namespace)
    #-------------------------------------------------------------------------------
