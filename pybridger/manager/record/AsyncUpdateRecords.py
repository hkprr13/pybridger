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
            tableName  : str,
            columns    : str,
            data       : list[tuple[str]],
            conditions : str,
        ) -> None:
        """
        Initalize condition object
        Args:
            tableName  (str)   : table name
            columns    (str)   : columns for updates
            values     (tuple) : values
            conditions (str)   : conditons for updates
        """
        super().__init__(tableName)
        query = f"UPDATE {tableName} SET {columns}" \
              + f"WHERE {conditions};"
        self.query = query.replace("?", self.sqlEngine.PLACEHOLDER)
        self.data = data
#-------------------------------------------------------------------------------
class AsyncUpdateRecords(AsyncBase):
    """
    Define a record update class
    """
    def __init__(
            self,
            tableName : str,
            columns   : str,
            data      : list[tuple[str]]  
        ) -> None:
        """
        Define a record update class
        """
        super().__init__(tableName)
        self.__columns   = columns
        self.__data      = data
    #---------------------------------------------------------------------------
    @ public
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
        datas      = []
        for key, values in conditionsColumn.items():
            conditions += f"{key} = ?"
            # Make it available for use as a placeholder
            for i in range(len(values)):
                data = list(self.__data[i]) # Change to a list type 
                                            # so that it can be appended
                data.append(values[i])      # Add data to the end 
                                            # so that it can be used as a placeholder
                datas.append(tuple(data))   # Change to tuple type and add to list
        return Where(
            tableName  = self.tableName,
            columns    = self.__columns,
            data       = datas,
            conditions = conditions,
        )
#-------------------------------------------------------------------------------
