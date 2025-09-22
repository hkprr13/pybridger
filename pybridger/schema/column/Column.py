#-------------------------------------------------------------------------------
from typing         import Any
from ..datatypes    import DataType
from ..constraints  import AutoIncrement
from ..constraints  import PrimaryKey
from ..constraints  import Default
from ..constraints  import NotNull
from ..constraints  import Unique
from ..constraints  import Check
from ..constraints  import TableLevelCheck
from ..constraints  import ForeignKey
from ...common      import public
from ...common      import private
from ..conditions   import Condition
from ..conditions   import ConditionGroup
from ...mapper      import Query
from ...errors      import DataTypeUndefinedError
#-------------------------------------------------------------------------------
class Column:
    """
    Define the columns and column information
    """
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
    ) -> None:
        """
        Initialize column object 
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
            User(Model):
                id = Column(
                    dataType        = Integer(),
                    isPrimaryKey    = True,
                    isAutoIncrement = True,
            )
            ```
            
        """
        # public attributes (table and column)
        self.__columnName__   : str 
        self.__tableName__    : str 
        self.referencedTable  : str | None = None
        self.referencedColumn : str | None = None
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
        # Data types in Python
        self.PYTHON_TYPE : str = self.__dataType.PYTHON_TYPE
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
    @private
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
    @private
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
    @private
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
    @private
    def __buildDefaultQuery(self) -> Any | Query:
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
    @private
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
    @public
    def buildTableLevelCheckQuery(self) -> Query:
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
    @public
    def buildForeignKeyQuery(self) -> Query:
        """
        Build query for foreign key constraints.
        Setting referenced table and column
        Returns:
            Query : query object
        """
        if self.__foreignKey:
            self.referencedTable  = self.__foreignKey.referencedTable
            self.referencedColumn = self.__foreignKey.referencedColumn
            fk = self.__foreignKey.toQuery().sql
            fk = fk.replace("~~~", self.__columnName__)
            return Query(fk)
        else:
            return Query("")
    #---------------------------------------------------------------------------
    @public
    def buildCreateList(self) -> list:
        """
        Build create table query
        Returns:
            Query : use for create table query 
        """
        parts = []
        parts.append(self.__columnName__)
        parts.append(self.dataTypeQuery.sql)
        if self.primaryKeyQuery.sql:
            parts.append(self.primaryKeyQuery.sql)
        if self.autoIncrementQuery.sql:
            parts.append(self.autoIncrementQuery.sql)
        if self.notNullQuery.sql:
            parts.append(self.notNullQuery.sql)
        if self.defaultQuery.sql:
            parts.append(self.defaultQuery.sql)
        if self.checkQuery.sql:
            parts.append(self.checkQuery.sql)
        return parts
    #---------------------------------------------------------------------------
    def setTableName(self, tableName : str) -> None:
        """
        Setter.
        Setting table name in class
        Args:
            tableName (str) : table name
        """
        self.__tableName__ = tableName
    #---------------------------------------------------------------------------
    def getTableName(self) -> str | None:
        """
        Getter.
        Getting table name for class
        Returns:
            str | None : If not set, return None
        """
        return self.__tableName__ 
    #---------------------------------------------------------------------------
    def setColumnName(self, columnName : str) -> None:
        """
        Setter.
        Setting column name in class
        Args:
            columnName (str) : column name
        """
        self.__columnName__ = columnName
    #---------------------------------------------------------------------------
    def getColumnName(self) -> str | None:
        """
        Getter.
        Getting table name for class
        Returns:
            str | None : If not set, return None.
        """
        return self.__columnName__
    #---------------------------------------------------------------------------
    @public
    def toQuery(self) -> tuple[str, list]:
        if hasattr(self, "__tableName__") and hasattr(self, "__columnName__"):
            query = f"{self.__tableName__}.{self.__columnName__}"
        else:
            query = f"{self.__columnName__}"
        return query, []
    #---------------------------------------------------------------------------
    @public
    def like(self, value) -> Condition:
        """LINK operator"""
        return Condition(
            self.__tableName__, self.__columnName__, "LIKE", value
        )
    #---------------------------------------------------------------------------
    @public
    def In (self, *values) -> Condition:
        """IN operator"""
        return Condition(
            self.__tableName__, self.__columnName__, "IN", values
        )
    #---------------------------------------------------------------------------
    @public
    def notIn (self, *values) -> Condition:
        """NOT IN operator"""
        return Condition(
            self.__tableName__, self.__columnName__, "NOT IN", (values)
        )
    #---------------------------------------------------------------------------
    @public
    def between(self, before, after) -> Condition:
        """BETWEEN operator"""
        return Condition(
            self.__tableName__, self.__columnName__,
            "BETWEEN",          (before, after)
        )
    #---------------------------------------------------------------------------
    def __eq__(self, value) -> Condition:
        """
        equivalent comparison
        Returns:
            Condition : condition
        """
        return Condition(self.__tableName__, self.__columnName__, "=", value)
    #---------------------------------------------------------------------------
    def __ne__(self, value) -> Condition:
        """
        inequality comparison
        Returns:
            Condition : condition
        """
        return Condition(self.__tableName__, self.__columnName__, "!=", value)
    #---------------------------------------------------------------------------
    def __lt__(self, value) -> Condition:
        """
        less than
        Returns:
            Condition : condition
        """
        return Condition(self.__tableName__, self.__columnName__, "<", value)
    #---------------------------------------------------------------------------
    def __le__(self, value) -> Condition:
        """
        Below
        Returns:
            Condition : condition
        """
        return Condition(self.__tableName__, self.__columnName__, "<=", value)
    #---------------------------------------------------------------------------
    def __gt__(self, value) -> Condition:
        """
        Greater than
        Returns:
            Condition : condition
        """
        return Condition(self.__tableName__, self.__columnName__, ">", value)
    #---------------------------------------------------------------------------
    def __ge__(self, value) -> Condition:
        """
        Above
        Returns:
            Condition : condition
        """
        return Condition(self.__tableName__, self.__columnName__, ">=", value)
    #---------------------------------------------------------------------------
    def __and__(self, value) -> ConditionGroup:
        """
        AND
        Returns:
            Condition : condition
        """
        return ConditionGroup(
            self.__tableName__, self.__columnName__, "AND", value
        )
    #---------------------------------------------------------------------------
    def __or__(self, value) -> ConditionGroup:
        """
        OR
        Returns:
            Condition : condition
        """
        return ConditionGroup(self.__tableName__, self.__columnName__, "OR", value)
#-------------------------------------------------------------------------------
