#-------------------------------------------------------------------------------
from .Filed             import Filed 
from ..datatypes        import Boolean
from ...common          import private
#-------------------------------------------------------------------------------
class BoolFiled(Filed):
    """
    Defile bool filed ckass
    """
    #---------------------------------------------------------------------------
    def __init__(
            self,
            default    : bool | None = None,
            foreignKey : str  | None = None
        ) -> None:
        """
        Initialization of the boolean column definition class
        Args:
            isNotNull  (bool)        : Whether to enable the NotNull constraint
            defalut    (bool | None) : Whether to set a default value 
                                     : None means unspecified,
                                     : True means the default value is True,
                                     : Flase means the default value is False
            foreignKey (str | None)  : Specifies the foreign key constraint
        Examples:
            ```
            isUpdate = BoolFiled(default = True)
            ```
        """
        super().__init__(
            dataType        = Boolean(),
            default         = self.__setDefalut(default),
            foreignKey      = foreignKey
        )
    #---------------------------------------------------------------------------
    @private
    def __setDefalut(self, defalut) -> None | str:
        if defalut is None:
            return None
        else:
            return str(defalut)
#-------------------------------------------------------------------------------