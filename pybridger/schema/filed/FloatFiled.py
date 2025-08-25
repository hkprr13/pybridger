#-------------------------------------------------------------------------------
from .Filed      import Filed
from ..datatypes import Float
#-------------------------------------------------------------------------------
class FloatFiled(Filed):
    """
    Define floating point filed class
    """
    def __init__(
            self,
            M          : int,  
            D          : int | None = None,
            check      : str | None = None,
            default    : str | None = None,
            foreignKey : str | None = None
        ) -> None:
        """
        Initialization of floating point column definitions
        Args:
            M          (int)        : decimal digits
            D          (int | None) : scale
            check      (str | None) : Whether to set a check value
            defalut    (str | None) : Whether to set a default value 
            foreignKey (str | None) : Specifies the foreign key constraint
        """
        super().__init__(
            dataType        = Float(M, D),
            check           = check,
            default         = default,  
            foreignKey      = foreignKey 
        )
#-------------------------------------------------------------------------------