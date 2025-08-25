#-------------------------------------------------------------------------------
from ..AsyncBase import AsyncBase
#-------------------------------------------------------------------------------
class AsyncInsertRecord(AsyncBase):
    """
    Define a class for inserting records
    """
    def __init__(
            self,
            tableName    : str,
            columns      : str,
            values       : tuple,
            placeHolders : str
        ) -> None:
        """
        Initialize a class for inserting records object
        Args:
            tableName    (str)   : table name
            columns      (str)   : columns (id, name, age)
            values       (tuple) : value (1, "name", 19)
            placeHolders (str)   : place holder
        """
        super().__init__(tableName)        
        placeHolders = placeHolders.replace(
            "?", self.sqlEngine.PLACEHOLDER
        )
        self.query = f"INSERT INTO {self.tableName} "\
                   + f"({columns}) VALUES ({placeHolders});"
        self.value = values
#-------------------------------------------------------------------------------