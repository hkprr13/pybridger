#-------------------------------------------------------------------------------
from .Filed      import Filed
from ..datatypes import Time 
#-------------------------------------------------------------------------------
class TimeFiled(Filed):
    """
    Define time filed
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
            defalut    (str | None) : Whether to set a default value 
            foreignKey (str | None) : Specifies the foreign key constraint
        """
        super().__init__(
            dataType        = Time(),
            check           = check,
            default         = default,  
            foreignKey      = foreignKey 
        )
#-------------------------------------------------------------------------------