#-------------------------------------------------------------------------------
from typing         import Any, Literal
from typing         import LiteralString
from ..Base         import Base
from .GroupBy       import GroupBy
from .Where         import Where
from .join          import CrossJoin
from .join          import FullOuterJoin
from .join          import InnerJoin
from .join          import LeftJoin
from .join          import NaturalJoin
from .join          import RightJoin
from .join          import SelfJoin
from ...schema      import Column
from ...schema      import Condition
from ...schema      import ConditionGroup 
from ...common      import public
from ...common      import private 
from ...model       import Model
#-------------------------------------------------------------------------------
class Select(Base):
    """
    Define select object
    """
    #---------------------------------------------------------------------------
    def __init__(
            self,
            tableName  : str, 
            columns,
        ) -> None:
        """"
        Initialize select object
        Args:
            tableName (str) : table name
            columns   (str) : column
        """
        super().__init__(tableName)
        self.__columns     = self.__setColumns(columns)
        self.__columnsList = self.__setColumnsList(columns)
        self.__query   = ""
    #---------------------------------------------------------------------------
    @private
    def __setColumns(self, columns) -> LiteralString | Literal['*']:
        # If columns is not specified as an argument, it is recognized as *.
        if len(columns) == 0:
            cols = "*"
        else:
            cols = ", ".join(col.__columnName__ for col in columns)
        return cols
    #---------------------------------------------------------------------------
    @private
    def __setColumnsList(self, columns : tuple[Column]):# -> list[Any]:
        columnsList = []
        for col in columns:
            columnsList.append(f"{col.__tableName__}.{col.__columnName__}")
        return columnsList
    #---------------------------------------------------------------------------
    @public
    def getRecord(self) -> list:
        """
        Retrieves all records from the specified column.
        Returns:
            List : List of query result records.
        """
        self.__query = f"SELECT {self.__columns} FROM {self.tableName};"
        cur = self.sqlEngine.cursor()
        cur.execute(self.__query)
        return cur.fetchall()
    #---------------------------------------------------------------------------
    @public
    def getAllRecord(self) -> list:
        """
        Retrieve all records from all columns in the table
        Returns:
            List : Query result record list
        """
        self.__query = f"SELECT * FROM {self.tableName};"
        cur = self.sqlEngine.cursor()
        cur.execute(self.__query)
        return cur.fetchall()
    #---------------------------------------------------------------------------
    @public
    def where(
            self,
            *condition : Condition | ConditionGroup
        )-> Where:
        """
        WHERE
        Args:
            *condition (Condition | ConditionGroup) : conditon
        Examples:
            engine = Engine(...)
            engine.launch()
            user   = engine.select(User, User.id, User.name)
            result = user.where((User.age >= 20) & (User.age <= 29)).fetchall()
        """
        placeHolder = self.sqlEngine.PLACEHOLDER
        parts  = []
        values = []
        for cond in condition:
            sql, vals = cond.toQuery(placeHolder)
            parts.append(sql)
            values.extend(vals)
        whereClause = " AND ".join(parts)
        values = tuple(values)            
        return Where(
            tableName = self.tableName,
            columns   = self.__columns,
            condition = whereClause,
            value     = values
        )
    #---------------------------------------------------------------------------  
    @public
    def orderBy(
            self,
            asc  : Column | None = None, # ascending order
            desc : Column | None = None, # descending order
        ) -> list:
        """
        Sort data in ascending or descending order
        Args:
            asc  (Column) : Column to sort in ascending order
            desc (Column) : Column to sort in descending order
        Returns:
            list : List of records after sorting.
        """
        query = f"SELECT {self.__columns} FROM {self.tableName} "
        if asc is None and desc is None:
            raise Exception("Please specify either asc or desc")
        if asc is None and not desc is None:
            query += f"ORDER BY {desc.__columnName__} DESC;"
        if not asc is None and desc is None:  
            query += f"ORDER BY {asc.__columnName__} ASC;"
        if not desc is None and not asc is None:
            query += f"ORDER BY {asc.__columnName__} ASC, {desc.__columnName__} DESC;"
        cur = self.cursor()
        cur.execute(query)
        self.__query = query
        return cur.fetchall()
    #---------------------------------------------------------------------------
    @public
    def limitOffset(
            self,
            limit  : int,
            offset : int
        ) -> list:
        """
        Retrieve paginated records using LIMIT and OFFSET.
        Args:
            limit  (int) : Maximum number of records to retrieve.
            offset (int) : Starting position for retrieval.
        Returns:
            list : Part of the query results.
        """
        query = f"SELECT {self.__columns} " \
              + f"FROM {self.tableName} " \
              + f"LIMIT {limit} OFFSET {offset}"
        cur = self.sqlEngine.cursor()
        cur.execute(query)
        self.__query = query
        return cur.fetchall()
    #---------------------------------------------------------------------------  
    @public
    def count(self) -> list[Any] | Any:
        """
        Get the number of records
        Returns:
        int: Tuple of number of records
        """
        self.__query = f"SELECT COUNT(*) " \
                     + f"FROM {self.tableName} "
        cur = self.sqlEngine.cursor()
        cur.execute(self.__query)
        return cur.fetchall()
    #---------------------------------------------------------------------------
    @public
    def getAvg(
            self,
            column : Column
        ) -> list[Any] | Any:
        """
        Get the average value of the specified column
        Returns:
            List[Tuple]: Tuple of average values (e.g., [(34.5,]))
        """
        self.__query = f"SELECT AVG({column.__columnName__}) " \
                     + f"FROM {self.tableName} "    
        cur = self.sqlEngine.cursor()
        cur.execute(self.__query)
        return cur.fetchall()
    #---------------------------------------------------------------------------
    @public
    def getSum(
            self,
            column : Column
        ) -> list[Any] | Any:
        """
        Get the sum of the specified column
        Args:
            column (Column) : Target column
        Returns:
            List[Tuple] : Tuple of sum values
        """
        self.__query = f"SELECT SUM({column.__columnName__}) " \
                     + f"FROM {self.tableName} "    
        cur = self.sqlEngine.cursor()
        cur.execute(self.__query)
        return cur.fetchall()
    #---------------------------------------------------------------------------
    @public
    def getMax(
            self,
            column : Column
        ) -> list[Any] | Any:
        """
        Get the maximum value of the specified column.
        Args:
            column (Column) : Target column
        Returns:
            List[Tuple] : Tuple of maximum values
        """
        self.__query = f"SELECT Max({column.__columnName__}) " \
                     + f"FROM {self.tableName} "    
        cur = self.sqlEngine.cursor()
        cur.execute(self.__query)
        return cur.fetchall()
    #---------------------------------------------------------------------------
    @public
    def getMin(
            self,
            column : Column
        ) -> list[Any] | Any:
        """
        Get the minimum value of the specified column
        Args:
            column (Column) : Target column
        Returns:
            List[Tuple] : Tuple of minimum values
        """
        self.__query = f"SELECT Min({column.__columnName__}) " \
                     + f"FROM {self.tableName} "    
        cur = self.sqlEngine.cursor()
        cur.execute(self.__query)
        return cur.fetchall()
    #---------------------------------------------------------------------------
    @public
    def groupBy(
            self,
            column : Column  
        ) -> GroupBy:
        """
        Execute GROUP BY on the specified column.
        Args:
            column (Column) : Column to be grouped.
        Returns:
            GroupBy : Grouping query object.
        """
        return GroupBy(
            tableName = self.tableName,
            columns   = self.__columns,
            condition = "",
            byColumn  = column.__columnName__
        )
    #---------------------------------------------------------------------------
    @public
    def whereGroupBy(
            self,
            condition, 
            column : Column  
        ) -> GroupBy:
        """
        Conditional grouping using WHERE + GROUP BY clause
        Args:
            condition (str) : WHERE condition
            column    (Column) : Column to be grouped
        Returns:
            GroupBy : Grouping query object
        """
        return GroupBy(
            tableName = self.tableName,
            columns   = self.__columns,
            condition = condition,
            byColumn  = column.__columnName__
        )
    #---------------------------------------------------------------------------
    @public
    def crossJoin(
            self,
            joinTable : type[Model],
        ) -> CrossJoin:
        """
        CROSS JOIN method
        Args:
            joinTable (type[Model]) : table model object
            conditon  (Conditon)    : conditon
        Returns:
            CrossJoin : Cross join object 
        """
        return CrossJoin(
            tableName = self.tableName,
            joinTable = joinTable.__tableName__
        )
    #---------------------------------------------------------------------------
    @public
    def fullOuterJoin(
            self,
            joinTable : type[Model],
            *condition   : Condition
        ) -> FullOuterJoin:
        """
        FULL OUTER JOIN method
        Args:
            joinTable (type[Model]) : table model object
            c
        Returns:
            FullOuterJoin : Full outer join object 
        """
        placeHolder = self.sqlEngine.PLACEHOLDER
        parts  = []
        for cond in condition:
            sql, vals = cond.toQuery(placeHolder)
            parts.append(sql)
        joinSql = " AND ".join(parts)
        return FullOuterJoin(
            tableName = self.tableName,
            joinTable = joinTable.__tableName__,
            joinSql   = joinSql
        )
    #---------------------------------------------------------------------------
    @public
    def innerJoin(
            self,
            joinTable  : type[Model],
            *condition : Condition
        ) -> InnerJoin:
        """
        INNER JOIN method
        Args:
            joinTable (type[Model]) : table model object
            conditon  (Conditon)    : conditon
        Returns:
            InnerJoin : Inner join object 
        """
        placeHolder = self.sqlEngine.PLACEHOLDER
        parts  = []
        for cond in condition:
            sql, vals = cond.toQuery(placeHolder)
            parts.append(sql)
        joinSql = " AND ".join(parts)
        return InnerJoin(
            tableName = self.tableName,
            columns   = self.__columns,
            joinTable = joinTable.__tableName__,
            joinSql   = joinSql
        )
    #---------------------------------------------------------------------------
    @public
    def leftJoin(
            self,
            joinTable  : type[Model],
            *condition : Condition
        ) -> LeftJoin:
        """
        LEFT JOIN method
        Args:
            joinTable (type[Model]) : table model object
            conditon  (Conditon)    : conditon
        Returns:
            LeftJoin : Left join object 
        """
        columns = ""
        for col in self.__columnsList:
            columns += f"{col}, "
        columns = columns[:-2]
        placeHolder = self.sqlEngine.PLACEHOLDER
        parts  = []
        for cond in condition:
            sql, vals = cond.toQuery(placeHolder)
            parts.append(sql)
        joinSql = " AND ".join(parts)
        return LeftJoin(
            tableName  = self.tableName,
            columns    = columns,
            joinTable  = joinTable.__tableName__,
            joinSql    = joinSql
        )
    #---------------------------------------------------------------------------
    @public 
    def naturalJoin(
            self,
            joinTable  : type[Model],
        ) -> NaturalJoin:
        """
        NATURAL JOIN method
        Args:
            joinTable (type[Model]) : table model object
            conditon  (Conditon)    : conditon
        Returns:
            NaturalJoin : Natural join object 
        """
        return NaturalJoin(
            tableName = self.tableName,
            columns   = self.__columns,
            joinTable = joinTable.__tableName__,
        )
    #---------------------------------------------------------------------------
    @public
    def RightJoin(
            self,
            joinTable  : type[Model],
            *condition : Condition
        ) -> RightJoin:
        """
        RIGHT JOIN method
        Args:
            joinTable (type[Model]) : table model object
            conditon  (Conditon)    : conditon
        Returns:
            RightJoin : Right join object 
        """
        columns = ""
        for col in self.__columnsList:
            columns += f"{col}, "
        columns = columns[:-2]
        placeHolder = self.sqlEngine.PLACEHOLDER
        parts  = []
        for cond in condition:
            sql, vals = cond.toQuery(placeHolder)
            parts.append(sql)
        joinSql = " AND ".join(parts)
        return RightJoin(
            tableName  = self.tableName,
            columns    = columns,
            joinTable  = joinTable.__tableName__,
            joinSql    = joinSql
        )
    #---------------------------------------------------------------------------
    @public
    def selfJoin(
            self
        ): ...
#-------------------------------------------------------------------------------