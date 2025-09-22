#-------------------------------------------------------------------------------
from typing             import Literal
from .PybridgerError    import PyBridgerError
#-------------------------------------------------------------------------------
class DatabaseUndefinedError(PyBridgerError):
    def __init__(self) -> None:
        super().__init__()
    #---------------------------------------------------------------------------
    @property
    def msg(self) -> Literal["Database un defined"]:
        return "Database un defined" 
#-------------------------------------------------------------------------------