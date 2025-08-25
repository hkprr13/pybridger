#-------------------------------------------------------------------------------
from .Filed      import Filed
from ..datatypes import DateTime
#-------------------------------------------------------------------------------
class DateTimeFiled(Filed):
    """
    時間型のカラム定義クラス
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
            isNotNull  (bool)       : Whether to enable the NotNull constraint
            defalut    (str | None) : Whether to set a default value   
            foreignKey (str | None) : Specifies the foreign key constraint
        """
        super().__init__(
            dataType        = DateTime(),
            default         = default,
            check           = check,  
            foreignKey      = foreignKey
        )
#-------------------------------------------------------------------------------