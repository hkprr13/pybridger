#-------------------------------------------------------------------------------
import sys
from typing             import Literal
#-------------------------------------------------------------------------------
def custom_excepthook(exc_type, exc_value, traceback):
    print(f"{exc_type.__name__}: {exc_value}")
sys.excepthook = custom_excepthook
#-------------------------------------------------------------------------------
class PyBridgerError(Exception):
    def __init__(self) -> None:
        
        super().__init__(self.msg)
    @property
    def msg(self) -> Literal["pybridger error"]:
        return "pybridger error"
#-------------------------------------------------------------------------------
