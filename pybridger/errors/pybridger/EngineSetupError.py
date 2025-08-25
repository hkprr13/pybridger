#-------------------------------------------------------------------------------
from typing import Literal
from .PybridgerError import PyBridgerError
#-------------------------------------------------------------------------------
class EngineSetupError(PyBridgerError):
    def __init__(self) -> None:
        super().__init__()
    #---------------------------------------------------------------------------
    @property
    def msg(self) -> Literal["An error occurred during engine of SQL setup"]:
        return "An error occurred during engine of SQL setup" 
#-------------------------------------------------------------------------------