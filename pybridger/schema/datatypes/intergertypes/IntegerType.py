#-------------------------------------------------------------------------------
from typing         import Any
from ..datatype     import DataType
#-------------------------------------------------------------------------------
class IntegerType(DataType):
    def __init__(self) -> None:
        super().__init__()
        self.storage              : Any
        self.signedMaximum        : Any
        self.signedMinimum        : Any
        self.maximumUnsignedValue : Any
        self.minimumUnsignedValue : Any
    #---------------------------------------------------------------------------
    def getStorage(self) -> Any:
        return self.storage
    #---------------------------------------------------------------------------
    def getSignedMaximum(self) -> Any:
        return self.signedMaximum
    #---------------------------------------------------------------------------
    def getSignedMinimum(self) -> Any:
        return self.signedMinimum
    #---------------------------------------------------------------------------
    def getMaximumUnsignedValue(self) -> Any:
        return self.maximumUnsignedValue()
    #---------------------------------------------------------------------------
    def getMinimumUnsignedValue(self) -> Any:
        return self.minimumUnsignedValue()
#-------------------------------------------------------------------------------