#-------------------------------------------------------------------------------
from typing         import Any                  # Any型
from .IntegerType   import IntegerType          # 整数型
from ...common      import override             # オーバライドデコレーター
from ...common      import private              # パブリックデコレーター
from ...query       import Query                # クエリクラス
#-------------------------------------------------------------------------------
class SmallInt(IntegerType):
    """
    2バイト整数型
    サポートされているSQL(MySQL, PostgreSQL)
    """
    #---------------------------------------------------------------------------
    @override
    @private
    def mysql(self):
        self.query                : Any = Query("SMALLINT")
        self.storage              : Any =       2
        self.signedMaximum        : Any =  32,767
        self.signedMinimum        : Any = -32,768
        self.maximumUnsignedValue : Any =  65,535
        self.minimumUnsignedValue : Any =       0
    #---------------------------------------------------------------------------
    @override
    @private
    def sqlite3(self):
        self.query                : Any = self.TEXTNOTSUPPORTED
        self.storage              : Any = self.TEXTNOTSUPPORTED
        self.signedMaximum        : Any = self.TEXTNOTSUPPORTED
        self.signedMinimum        : Any = self.TEXTNOTSUPPORTED
        self.maximumUnsignedValue : Any = self.TEXTNOTSUPPORTED
        self.minimumUnsignedValue : Any = self.TEXTNOTSUPPORTED
    #---------------------------------------------------------------------------
    @override
    @private
    def postgresql(self):
        self.query                : Any = Query("SMALLINT")
        self.storage              : Any =       2
        self.signedMaximum        : Any =  32,767
        self.signedMinimum        : Any = -32,768
        self.maximumUnsignedValue : Any = self.TEXTNOTSUPPORTED
        self.minimumUnsignedValue : Any = self.TEXTNOTSUPPORTED
#-------------------------------------------------------------------------------