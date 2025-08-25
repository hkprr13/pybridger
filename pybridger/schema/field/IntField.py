#-------------------------------------------------------------------------------
from .Field      import Field   # 基底クラス
from ..datatypes import Integer # 整数型
#-------------------------------------------------------------------------------
class IntField(Field):
    """
    Define integer field
    """
    def __init__(
            self,
            isPrimaryKey    : bool        = False,
            isUnique        : bool        = False,
            isAutoincrement : bool        = False,
            check           : str  | None = None,
            default         : str  | None = None,
            foreignKey      : str  | None = None
        ) -> None:
        """
        Initialization of integer column definitions
        Args:
            isPrimaryKey    (bool)       : Primary key setting
            isUnique        (bool)       : Set unique constraint
            isAutoincrement (bool)       : Set auto-increment
            check           (str | None) : Whether to set a check value 
            default         (str | None) : Set default value
            foreignKey      (str | None) : Set foreign key constraint
        """
        super().__init__(
            dataType        = Integer(),
            isPrimaryKey    = isPrimaryKey,
            isUnique        = isUnique,
            isAutoincrement = isAutoincrement,
            check           = check,
            default         = default,
            foreignKey      = foreignKey
        )
#-------------------------------------------------------------------------------