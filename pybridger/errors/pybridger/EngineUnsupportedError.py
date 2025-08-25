#-------------------------------------------------------------------------------
from typing import Literal
from .PybridgerError import PyBridgerError
#-------------------------------------------------------------------------------
class EngineUnsupportedError(PyBridgerError):
    def __init__(self) -> None:
        super().__init__()
    #---------------------------------------------------------------------------
    @property
    def msg(self) -> Literal['Unsupported Engine']:
        return "Unsupported Engine" 
#-------------------------------------------------------------------------------