#-------------------------------------------------------------------------------
from .Field      import Field
from ..datatypes import Text 
#-------------------------------------------------------------------------------
class StrField(Field):
    """
    Define String Field
    """
    def __init__(
            self,
            isPrimaryKey    : bool        = False,
            isUnique        : bool        = False,
            check           : str  | None = None,
            default         : str  | None = None,
            foreignKey      : str  | None = None
        ) -> None:
        """
         Initialization of string type column definitions
        Args:
            isPrimaryKey    (bool)       : Primary key setting
            isUnique        (bool)       : Set unique constraint
            check           (str | None) : Whether to set a check value 
            default         (str | None) : Set default value
            foreignKey      (str | None) : Set foreign key constraint
        """
        super().__init__(
            dataType        = Text(),
            isPrimaryKey    = isPrimaryKey,  
            isUnique        = isUnique,
            check           = check,
            default         = default, 
            foreignKey      = foreignKey 
        )
#-------------------------------------------------------------------------------