#-------------------------------------------------------------------------------
from ..datatypes    import DataType
from ..constraints  import AutoIncrement      # 自動採番 
from ..constraints  import PrimaryKey         # 主キークラス
from ..constraints  import Default            # デフォルト値クラス
from ..constraints  import NotNull            # NotNullクラス
from ..constraints  import Unique             # ユニーク設定クラス
from ..constraints  import Check              # CHECK制約クラス
from ..constraints  import TableLevelCheck    # CHCEK制約(テーブルレベル)
from ..constraints  import ForeignKey         # 外部キー制約クラス
from ...common      import public             # パブリックメソッド
from ...common      import private            # プライベートメソッド
from ..conditions   import Condition          # 条件クラス
from ..conditions   import ConditionGroup     # 条件クラス
from ...mapper      import Query
from ...errors      import DataTypeUndefinedError
#-------------------------------------------------------------------------------
class Column:
    """
    Define the columns and column information
    """
    #---------------------------------------------------------------------------

    #---------------------------------------------------------------------------
    def __init__(
        self,
        dataType        : DataType,
        isPrimaryKey    : bool                   = False,
        isAutoIncrement : bool                   = False,
        isNotNull       : bool                   = False,
        isUnique        : bool                   = False,
        default         : Default         | None = None,
        check           : Check           | None = None,
        tableLevelCheck : TableLevelCheck | None = None,
        foreignKey      : ForeignKey      | None = None
    ):
        """
        Intialize column object 
        Args:
            dataType        (DataType)               : Define data type
            isPrimaryKey    (bool)                   : Enable primary key or not
            isAutoIncrement (bool)                   : Enable auto increment or not
            isNotNull       (bool)                   : Enable not null constraint or not
            isUnique        (bool)                   : Enable unique constraint or not
            default         (Default         | None) : Define default values. If None, it is undefined
            check           (Check           | None) : Define check constraints. If None, it is undefined.
            tableLevelCheck (TableLevelCheck | None) : Define table-level check constraints. If None, it is undefined.
            foreignKey      (ForeignKey      | None) : Define foreign keys. If None, it is undefined.
        Raises:
            ValueError : When the data type is undefined
        Examples:
            ```
                
            ```
            
        """

        # private attributes
        self.__dataType        = dataType
        self.__isPrimaryKey    = isPrimaryKey
        self.__isAutoIncrement = isAutoIncrement
        self.__isNotNull       = isNotNull
        self.__isUnique        = isUnique
        self.__default         = default
        self.__check           = check
        self.__tableLevelCheck = tableLevelCheck
        self.__foreignKey      = foreignKey
        # public attributes (query)
        self.dataTypeQuery        : Query = self.__buildDataTypeQuery()
        self.primaryKeyQuery      : Query = self.__buildPrimaryKeyQuery()
        self.autoIncrementQuery   : Query = self.__buildAutoIncrementQuery()
        self.notNullQuery         : Query = self.__buildNotNullQuery()
        self.uniqueQuery          : Query = self.__buildUniqueQuery()
        self.defaultQuery         : Query = self.__buildDefaultQuery()
        self.checkQuery           : Query = self.__buildCheckQuery()
        self.tableLevelCheckQuery : Query = self.__buildTableLevelCheckQuery()
        self.foreignKeyQuery      : Query = 
        # public attributes (column name & table name)
        self.columnName : str
        self.tableName  : str 
    #---------------------------------------------------------------------------
    @private
    def __buildDataTypeQuery(self) -> Query:
        """
        private method
        build query for data type
        Returns:
            Query : query object
        Raises:
            DataTypeUndefinedError : When data type is undefined
        """
        try:
            query = self.__dataType.toQuery()
            return query
        except Exception:
            raise DataTypeUndefinedError()
    #---------------------------------------------------------------------------
    @private
    def __buildPrimaryKeyQuery(self) -> Query:
        """
        private method
        build query for primary key
        Returns:
            Query : query object
        """
        if self.__isPrimaryKey:
            primaryKey = PrimaryKey()
            return primaryKey.toQuery()
        else:
            return Query("")
    #---------------------------------------------------------------------------
    def __buildAutoIncrementQuery(self) -> Query:
        """
        private method
        build query for auto increment
        Returns:
            Query : query object
        """
        if self.__isAutoIncrement:
            autoIncrement = AutoIncrement()
            return autoIncrement.toQuery()
        else:
            return Query("")
    #---------------------------------------------------------------------------
    def __buildNotNullQuery(self) -> Query:
        """
        private method
        build query for not null constraints
        Returns:
            Query : query object
        """
        if self.__isNotNull:
            notNull = NotNull()
            return notNull.toQuery()
        else:
            return Query("")
    #---------------------------------------------------------------------------
    def __buildUniqueQuery(self) -> Query:
        """
        private method
        build query for unique constraints
        Returns:
            Query : query object
        """
        if self.__isUnique:
            unique = Unique()
            return unique.toQuery()
        else:
            return Query("")
    #---------------------------------------------------------------------------
    def __buildDefaultQuery(self):
        """
        private method
        build query for default constraints
        Returns:
            Query : query object
        """
        if self.__default:
            return self.__default.toQuery()
        else:
            return Query("")
    #---------------------------------------------------------------------------
    def __buildCheckQuery(self) -> Query:
        """
        private method
        build query for check constraints
        Returns:
            Query : query object
        """
        if self.__check:
            return self.__check.toQuery()
        else:
            return Query("")
    #---------------------------------------------------------------------------
    def __buildTableLevelCheckQuery(self) -> Query:
        """
        private method
        build query for table-level check constraints
        Returns:
            Query : query object
        """
        if self.__tableLevelCheck:
            return self.__tableLevelCheck.toQuery()
        else:
            return Query("")
    #---------------------------------------------------------------------------
    def __buildForeignKeyQuery(self) -> Query:
        return Query("")
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
    @public
    def toQuery(self):
        if hasattr(self, "tableName") and hasattr(self, "columnName"):
            query = f"{self.tableName}.{self.columnName}"
        else:
            query = f"{self.columnName}"
        return query, []
    #---------------------------------------------------------------------------
    @public
    def like(self, value):
        """LIKE演算子"""
        return Condition(self.tableName, self.columnName, "LIKE", value)
    #---------------------------------------------------------------------------
    @public
    def In (self, *values):
        """IN演算子"""
        return Condition(self.tableName, self.columnName, "IN", values)
    #---------------------------------------------------------------------------
    @public
    def notIn (self, *values):
        """NOT IN演算子"""
        return Condition(self.tableName, self.columnName, "NOT IN", (values))
    #---------------------------------------------------------------------------
    @public
    def between(self, before, after):
        """BETWEEN演算子"""
        return Condition(
            self.tableName, self.columnName, "BETWEEN", (before, after)
        )
    #---------------------------------------------------------------------------
    def __str__(self) -> str:
        return self.columnName
    #---------------------------------------------------------------------------
    def __eq__(self, value):
        """
        等価比較演算子 ==
        """
        return Condition(self.tableName, self.columnName, "=", value)
    #---------------------------------------------------------------------------
    def __ne__(self, value):
        """
        不等比較演算子 !=
        """
        return Condition(self.tableName, self.columnName, "!=", value)
    #---------------------------------------------------------------------------
    def __lt__(self, value):
        """
        小なり演算子 <
        """
        return Condition(self.tableName, self.columnName, "<", value)
    #---------------------------------------------------------------------------
    def __le__(self, value):
        """
        以下演算子 <=
        """
        return Condition(self.tableName, self.columnName, "<=", value)
    #---------------------------------------------------------------------------
    def __gt__(self, value):
        """
        大なり演算子 >
        """
        return Condition(self.tableName, self.columnName, ">", value)
    #---------------------------------------------------------------------------
    def __ge__(self, value):
        """
        以上演算子 >=
        """
        return Condition(self.tableName, self.columnName, ">=", value)
    #---------------------------------------------------------------------------
    def __and__(self, value):
        """
        AND演算子 AND
        """
        return ConditionGroup(self.tableName, self.columnName, "AND", value)
    #---------------------------------------------------------------------------
    def __or__(self, value):
        """
        OR演算子 OR
        """
        return ConditionGroup(self.tableName, self.columnName, "OR", value)
#-------------------------------------------------------------------------------
