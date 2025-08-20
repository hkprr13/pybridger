#-------------------------------------------------------------------------------
from typing         import Any                  # Any型
from .IntegerType   import IntegerType          # 整数型
from ...common      import override             # オーバライドデコレーター
from ...common      import private              # パブリックデコレーター
from ...query       import Query                # クエリクラス
#-------------------------------------------------------------------------------
class BigInt(IntegerType):
    """
    8バイト整数型
    サポートされているSQL(MySQL, PostgreSQL)
    """
    #---------------------------------------------------------------------------
    @override
    @private
    def mysql(self):
        self.query                : Any = Query("BIGINT")
        self.storage              : Any =                          8
        self.signedMaximum        : Any =  9_223_372_036_854_775_807
        self.signedMinimum        : Any = -9_223_372_036_854_775_808
        self.maximumUnsignedValue : Any =                          0
        self.minimumUnsignedValue : Any = 18_446_744_073_709_551_615
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
        self.storage              : Any =                          8
        self.signedMaximum        : Any =  9_223_372_036_854_775_807
        self.signedMinimum        : Any = -9_223_372_036_854_775_808
        self.signedMinimum        : Any = self.TEXTNOTSUPPORTED
        self.maximumUnsignedValue : Any = self.TEXTNOTSUPPORTED
        self.minimumUnsignedValue : Any = self.TEXTNOTSUPPORTED
#-------------------------------------------------------------------------------