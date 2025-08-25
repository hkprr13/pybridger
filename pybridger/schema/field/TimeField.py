#-------------------------------------------------------------------------------
from .Field      import Field
from ..datatypes import Time 
#-------------------------------------------------------------------------------
class TimeField(Field):
    """
    Define time field
    """
    def __init__(
            self,
            check      : str | None = None,
            default    : str | None = None,
            foreignKey : str | None = None
        ) -> None:
        """
        Initialization of time-type column definition classes
        Args:
            check      (str | None) : Whether to set a check value 
            default    (str | None) : Whether to set a default value 
            foreignKey (str | None) : Specifies the foreign key constraint
        """
        super().__init__(
            dataType        = Time(),
            check           = check,
            default         = default,  
            foreignKey      = foreignKey 
        )
#-------------------------------------------------------------------------------