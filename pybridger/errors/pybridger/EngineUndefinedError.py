#-------------------------------------------------------------------------------
from typing             import Literal
from .PybridgerError    import PyBridgerError
#-------------------------------------------------------------------------------
class EngineUndefinedError(PyBridgerError):
    def __init__(self) -> None:
        super().__init__()
    #---------------------------------------------------------------------------
    @property
    def msg(self) -> Literal["SQL engine undefined"]:
        return "SQL engine undefined"
#-------------------------------------------------------------------------------
