#-------------------------------------------------------------------------------
from ..AsyncBase import AsyncBase
from ...common   import public
#-------------------------------------------------------------------------------
class Where(AsyncBase):
    """
    Condition class (for UpdateRecord)
    """
    def __init__(
            self,
            tableName    : str,
            columns      : str,
            values       : tuple,
            conditions   : str,
        ) -> None:
        """
        Initialize condition object
        Args:
            tableName  (str)   : table name
            columns    (str)   : columns for updates
            values     (tuple) : values
            conditions (str)   : conditons for updates
        """
        super().__init__(tableName)
        query = f"UPDATE {tableName} SET {columns} WHERE {conditions};"
        self.query = query.replace(
            "?", self.sqlEngine.PLACEHOLDER
        )
        self.value = values
#-------------------------------------------------------------------------------
class AsyncUpdateRecord(AsyncBase):
    """
    Define a record update class
    """
    #---------------------------------------------------------------------------
    def __init__(
            self,
            tableName    : str,
            columns      : str,
            values       : tuple,
        ) -> None:
        """
        Initialize a record update object
        """
        super().__init__(tableName)
        self.__columns = columns
        self.__values  = values
    #---------------------------------------------------------------------------
    @public
    async def where(self, **conditionsColumn) -> Where:
        """
        Method to update specified records
        Args:
            **conditionsColumn (str) : Specify the condition column you want to update
        Examples:
            ```
            user = User.updateRecord(name = "a", age = 20)
            user.where(id = 1) 
            user.execute()
            user.commit()
            ```
        Returns:
            Where : Returns where object
        """
        conditions = ""
        for key, value in conditionsColumn.items():
            conditions    += f"{key} = ?"
            self.__values += tuple(str(value))
        return Where(
            tableName    = self.tableName,
            columns      = self.__columns, 
            values       = self.__values,
            conditions   = conditions,
        )
#-------------------------------------------------------------------------------
