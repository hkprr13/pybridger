#-------------------------------------------------------------------------------
from typing     import Any
from ..Base     import Base
from ...common  import public
#-------------------------------------------------------------------------------
class Where(Base):
    """
    Define Where for SELECT class
    """
    def __init__(
            self,
            tableName : str,
            columns   : str,
            condition : str,
            value     : tuple
        ) -> None:
        """
        Initalize where for SELECT object
            tableName (str)   : table name
            columns   (str)   : column
            condition (str)   : condition
            value     (tuple) : value
        """
        super().__init__(tableName) 
        self.query = f"SELECT {columns} " \
                   + f"FROM {self.tableName} WHERE {condition};"
        self.value = value
    #---------------------------------------------------------------------------
    def inSubQuery(self, subQuery) -> list[Any] | Any:
        query  = self.query[:-1]
        sQuery = subQuery[:-1]
        query += f" IN ({sQuery});"
        cur = self.sqlEngine.cursor()
        cur.execute(query, self.value)
        return cur.fetchall()
    #---------------------------------------------------------------------------
    @public
    def fetchall(self) -> list[Any] | Any:
        """
        Fetchall
        """
        cur = self.sqlEngine.cursor()
        cur.execute(self.query, self.value)
        return cur.fetchall()
#-------------------------------------------------------------------------------