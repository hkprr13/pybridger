#-------------------------------------------------------------------------------
from ..AsyncBase import AsyncBase # 基底クラス
from ...common   import public    # パブリックメソッド
#-------------------------------------------------------------------------------
class AsyncInsertRecords(AsyncBase):
    """
    Define a class that inserts multiple records
    """
    def __init__(
            self,
            tableName    : str,
            columns      : str,
            data         : list[tuple[str]],
            placeHolders : str
        ) -> None:
        """
        Initalize a class that inserts multiple records object
        Args:
            tableName    (str)              : table name
            columns      (str)              : columns (id, name, age)
            data         (list[tuple[str]]) : values
                                              [(1,  2,  3 ),
                                               (a,  b,  c ),
                                               (19, 22, 17)]
            placeHolders (str)              : place holder
        """
        super().__init__(tableName)              
        placeHolders = placeHolders.replace(
            "?", self.sqlEngine.PLACEHOLDER
        )
        self.query = f"INSERT INTO {self.tableName} "\
                   + f"({columns}) VALUES ({placeHolders});"
        self.data = data
#-------------------------------------------------------------------------------