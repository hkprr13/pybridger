#-------------------------------------------------------------------------------
from .Constraint    import Constraint
from ...common      import override
from ...common      import private
from ...mapper      import Query
#-------------------------------------------------------------------------------
class ForeignKey(Constraint):
    """
    Defined foreign key constraint class
    """
    def __init__(
            self,
            referenceName : str,
            onUpdate      : bool | None = None,
            onDelete      : bool | None = None
        ):
        """
        Initialize foreign key constraint object
        Args:
            referenceName (str)         : It is the reference format of "table.column"
            onUpdate      (bool | None) : Whether or not to apply ON UPDATE CASCADE. If None, it is not specified. 
            onDelete      (bool | None) : Whether or not to apply ON DELETE CASCADE. If None, it is not specified. 
        Examples:
            ```
            ForeignKey(
                referenceName = "User.id"
                onUpdate      = True
                onDelete      = True
            )
            ```
        """
        self.__setReferenceName(referenceName)
        self.__onUpdate = onUpdate
        self.__onDelete = onDelete
    #---------------------------------------------------------------------------
    @private
    def __setReferenceName(self, referenceName : str):
        # Determine whether it is a string
        if not isinstance(referenceName, str):
            raise TypeError("The reference name must be a string")
        else: pass
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
        # SQL
        query = f"FOREIGN KEY (~~~) "\
            + f"REFERENCES {self.referencedTable}({self.referencedColumn})"
        if self.__onUpdate is None:
            pass # If None, query is not specified
        elif self.__onUpdate == True:
            query += " ON UPDATE CASCADE"
        else:
            query += " ON UPDATE NO ACTION"
        if self.__onDelete is None:
            pass # If None, query is not specified
        elif self.__onDelete == True:
            query += " ON DELETE CASCADE"
        else:
            query += " ON DELETE NO ACTION"
        return Query(query)
    #---------------------------------------------------------------------------
    @override
    def mysql(self) -> None:
        self.query  = self.__buildForeignKeyQuery()
    #---------------------------------------------------------------------------
    @override
    def sqlite3(self) -> None:
        self.query  = self.__buildForeignKeyQuery()
    #---------------------------------------------------------------------------
    @override
    def postgresql(self) -> None:
        self.query  = self.__buildForeignKeyQuery()
#-------------------------------------------------------------------------------