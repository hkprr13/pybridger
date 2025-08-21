#-------------------------------------------------------------------------------
from typing         import Any
from ..datatype     import DataType
from ....common     import public 
#-------------------------------------------------------------------------------
class DateTimeType(DataType):
    """
    Base Date time class
    """
    #---------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Initalize date time object
        Attributes:
            format (Any) : Date and time format
            range  (Any) : Date and time range
        """
        super().__init__()
        self.format : Any # Date and time format
        self.range  : Any # Date and time range
    #---------------------------------------------------------------------------
    @public
    def getFormat(self) -> Any:
        return self.format
#-------------------------------------------------------------------------------