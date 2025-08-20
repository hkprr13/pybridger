#-------------------------------------------------------------------------------
from typing         import Any                  # Any型
from ..datatype     import DataType             # データ型クラス
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