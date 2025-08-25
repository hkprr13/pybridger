#-------------------------------------------------------------------------------
from .Field      import Field
from ..datatypes import DateTime
#-------------------------------------------------------------------------------
class DateTimeField(Field):
    """
    Define date time field class
    """
    def __init__(
            self,
            default    : str  | None = None,
            check      : str  | None = None,
            foreignKey : str  | None = None
        ) -> None:
        """
        Initialization of time-type column definition classes
        Args:
            default    (str | None) : Whether to set a default value 
            check      (str | None) : Whether to set a check value 
            foreignKey (str | None) : Specifies the foreign key constraint
        """
        super().__init__(
            dataType        = DateTime(),
            default         = default,
            check           = check,  
            foreignKey      = foreignKey
        )
#-------------------------------------------------------------------------------