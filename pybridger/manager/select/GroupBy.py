#-------------------------------------------------------------------------------
from test.test_dataclasses import Any
from ..Base import Base
#-------------------------------------------------------------------------------
class GroupBy(Base):
    """
    Define a class that constructs and executes SQL GROUP BY syntax
    """
    #---------------------------------------------------------------------------
    def __init__(
            self,
            tableName : str,
            columns   : str,
            condition : str,
            byColumn  : str
        ) -> None:
        """
        Initalize a object that constructs and executes SQL GROUP BY syntax
        Args:
            tableName (str) : table name
            columns   (str) : columns 
            condition (str) : condition
            byColumn  (str) : by column
        """
        super().__init__(tableName)
        self.tableName = tableName
        self.columns   = columns
        self.condition = condition  
        self.byColumn  = byColumn
    #---------------------------------------------------------------------------
    def getRecord(self) -> list[Any] | Any:
        """
        Retrieve records using GROUP BY syntax
        Returns:
            List[Tuple] : List of grouped query results.
        """
        query = f"SELECT {self.columns} FROM {self.tableName} "
        if self.condition == "":
            query += f"GROUP BY {self.byColumn};"
        else:
            query += f"WHERE {self.condition} GROUP BY {self.byColumn};"
        cur = self.sqlEngine.cursor()
        cur.execute(query)
        return cur.fetchall()
    #---------------------------------------------------------------------------
    def having(self, aggregate) -> list[Any] | Any:
        """
        Use the GROUP BY + HAVING syntax
        to retrieve records with aggregation conditions
        Args:
            aggregate (Column) : Column with aggregation function
                                 used in the HAVING clause
        Examples
            Column("COUNT(*) > 1")
        Returns:
            List[Tuple] : List of query results after applying the HAVING clause
        """
        query = f"SELECT {self.columns} FROM {self.tableName} "
        if self.condition == "":
            query += f"GROUP BY {self.byColumn} "
        else:
            query += f"WHERE {self.condition} GROUP BY {self.byColumn} "
        query += f"HAVING {aggregate.columnName};"
        cur = self.sqlEngine.cursor()
        cur.execute(query)
        return cur.fetchall()
#-------------------------------------------------------------------------------
