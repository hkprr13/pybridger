#-------------------------------------------------------------------------------
from .Constraint    import Constraint
from ...common      import override
from ...common      import private
from ...common      import public
from ...mapper      import Query
#-------------------------------------------------------------------------------
class ForeignKey(Constraint):
    """
    Defined foreign key constraint class
    """
    __REFERENCEOPTIONS = {
        "CASCADE", "SET NULL", "SET DEFAULT", "NO ACTION", "RESTRICT"
    }
    def __init__(
            self,
            referenceName : str,
            onUpdate      : str | None = None,
            onDelete      : str | None = None,
        ) -> None:
        """
        Initialize foreign key constraint object
        Args:
            referenceName (str)        : It is the reference format of "table.column"
            onUpdate      (str | None) : reference option ["CASCADE", "SET NULL", "SET DEFAULT", "NO ACTION", "RESTRICT"]
            onDelete      (str | None) : reference option ["CASCADE", "SET NULL", "SET DEFAULT", "NO ACTION", "RESTRICT"]
        Examples:
            ```
            # Select one from the reference options
            # Example 1
            ForeignKey(
                referenceName = "User.id"
                onUpdate      = "CASCADE"
                onDelete      = "CASCADE"
            )
            # Example 2
            ForeignKey(
                referenceName = "User.id"
                onUpdate      = "CASCADE"
                onDelete      = "SET NULL"
            )
            ```
        """
        self.__setReferenceName(referenceName)
        self.__onUpdate = onUpdate
        self.__onDelete = onDelete

    #---------------------------------------------------------------------------
    @private
    def __setReferenceName(self, referenceName : str) -> None:
        """
        Setting reference name
        Args:
            referenceName (str) : reference name 
        Raises:
            TypeError  : If the reference name is not a string 
            ValueError : If the value is incorrect
        """
        # Determine whether it is a string
        if not isinstance(referenceName, str):
            raise TypeError("The reference name must be a string")
        strings : list = referenceName.split(".")
        # User.user_id
        if  len(strings) == 2:
            # referenced table 
            self.referencedTable  = strings[0] # User
            # referenced column 
            self.referencedColumn = strings[1] # user_id
        else:
            raise ValueError(
                f"The value'{referenceName}' is incorrect"
            )
    #---------------------------------------------------------------------------
    @private
    def __addAction(self, clause : str, action : str | None) -> str:
        """
        Add action
        Args:
            clause (str)        : "ON UPDATE" or "ON DELETE"
            action (str | None) : "CASCADE", "SET NULL", "SET DEFAULT",
                                  "NO ACTION", "RESTRICT"
        Raises:
            ValueError : If in action is not reference options 
        Returns:
            str : query 
        """
        if action is None:
            return ""
        if action.upper() not in self.__REFERENCEOPTIONS:
            raise ValueError(
                f"Invalid action {action}."
                f"Reference options: {self.__REFERENCEOPTIONS}"
            )
        return f" {clause} {action.upper()}"
    #---------------------------------------------------------------------------
    @private
    def __buildForeignKeyQuery(self) -> Query:
        """
        private method
        Build query for default
        Returns:
            Query : query

        Notes:
            Since it is output as FOREIGN KEY (~~~),
            it is necessary to replace ~~~ once the column name has been decided.
        """
        query = f"FOREIGN KEY (~~~) "\
              + f"REFERENCES {self.referencedTable}({self.referencedColumn})"
        query += self.__addAction("ON UPDATE", self.__onUpdate)
        query += self.__addAction("ON DELETE", self.__onDelete)
        self.query = Query(query)
        return self.query
    #---------------------------------------------------------------------------
    @public
    def setColumn(self, columnName : str) -> None:
        """
        Replace placeholder with actual column name
        Args:
            columnName (str) : column name to replace
        Raises:
            TypeError : If columnName is not a string
        """
        if not isinstance(columnName, str):
            raise TypeError("column name must be a string")
        self.query = Query(self.query.sql.replace("~~~", columnName))
    #---------------------------------------------------------------------------
    @override
    @public
    def mysql(self) -> None:
        self.query  = self.__buildForeignKeyQuery()
    #---------------------------------------------------------------------------
    @override
    @public
    def sqlite3(self) -> None:
        self.query  = self.__buildForeignKeyQuery()
    #---------------------------------------------------------------------------
    @override
    @public
    def postgresql(self) -> None:
        self.query  = self.__buildForeignKeyQuery()
#-------------------------------------------------------------------------------