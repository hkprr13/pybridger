#-------------------------------------------------------------------------------
from ..datatypes        import DataType
from ..column           import Column
from ..constraints      import Default
from ..constraints      import Check
from ..constraints      import ForeignKey
#-------------------------------------------------------------------------------
class Filed(Column):
    """
    Base class for field classes.
    Inherits column classes.
    Has more restrictions on settings than column classes
    """
    def __init__(
            self,
            dataType        : DataType,
            isPrimaryKey    : bool       = False,
            isAutoincrement : bool       = False,
            isNotNull       : bool       = False,
            isUnique        : bool       = False,
            check           : str | None = None,
            default         : str | None = None,
            foreignKey      : str | None = None
        ) -> None:
        """
        Initialize filed object
        Args:
            dataType        (DataType)   : Data type 
            isPrimaryKey    (bool)       : Defining the primary key
            isAutoincrement (bool)       : Defining autoincrement
            isNotNull       (bool)       : Defining not null
            isUnique        (bool)       : Defining unique
            check           (str | None) : Defining check
            default         (str | None) : Defining defalut
            foreignKey      (str | None) : Defining foreignkey
        """
        self.__foreignKey = foreignKey
        super().__init__(
            dataType        = dataType,
            isPrimaryKey    = isPrimaryKey,
            isAutoIncrement = isAutoincrement,
            isNotNull       = isNotNull,
            isUnique        = isUnique,
            default         = Default(default),
            check           = Check(check),
            foreignKey      = self.__setForeignKey()
        )
    #---------------------------------------------------------------------------
    def __setForeignKey(self) -> ForeignKey | None:
        if self.__foreignKey:
            return ForeignKey(self.__foreignKey)
        else:
            return None
#-------------------------------------------------------------------------------
