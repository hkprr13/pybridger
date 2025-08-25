#-------------------------------------------------------------------------------
from ..AsyncBase import AsyncBase # 基底クラス
from ...common   import public    # パブリックメソッド
#-------------------------------------------------------------------------------
class AsyncAlterTableAddColumn(AsyncBase):
    """
    Define a class to add columns to the table 
    """
    #---------------------------------------------------------------------------
    def __init__(
            self,
            tableName   : str,
            column      : str,
            dataType    : str,
            constraints : str,
        ) -> None:
        """
        Initialize a class to add columns to the table
        Args:
            tableName   (str) : table name
            column      (str) : column name
            dataType    (str) : data type
            constraints (str) : constraint
        """
        super().__init__(tableName)
        self.query = f"ALTER TABLE {tableName} ADD " \
                   + f"{column} {dataType} {constraints};"
#-------------------------------------------------------------------------------