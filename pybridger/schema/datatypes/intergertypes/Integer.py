#-------------------------------------------------------------------------------
from typing         import Any                  # Any型
from .IntegerType   import IntegerType          # 整数型
from ...common      import override             # オーバライドデコレーター
from ...common      import private              # パブリックデコレーター
from ...query       import Query                # クエリクラス
#-------------------------------------------------------------------------------
class Integer(IntegerType):
    """
    整数型
    サポートされているSQL(すべて)
    """
    #---------------------------------------------------------------------------
    @override
    @private
    def mysql(self):
        self.query                : Any = Query("INT")
        self.storage              : Any =              4
        self.signedMaximum        : Any =  2_147_483_647
        self.signedMinimum        : Any = -2_147_483_648
        self.maximumUnsignedValue : Any =  4_294_967_295
        self.minimumUnsignedValue : Any =              0
    #---------------------------------------------------------------------------
    @override
    @private
    def sqlite3(self):
        self.query                : Any = Query("INTEGER")
        self.storage              : Any =  "1~8"
        self.signedMaximum        : Any = -9_223_372_036_854_775_808
        self.signedMinimum        : Any =  9_223_372_036_854_775_807
        self.maximumUnsignedValue : Any = self.TEXTNOTSUPPORTED
        self.minimumUnsignedValue : Any = self.TEXTNOTSUPPORTED
    #---------------------------------------------------------------------------
    @override
    @private
    def postgresql(self):
        self.query                : Any = Query("INT")
        self.storage              : Any =              4
        self.signedMaximum        : Any =  2_147_483_647
        self.signedMinimum        : Any = -2_147_483_648
        self.maximumUnsignedValue : Any = self.TEXTNOTSUPPORTED
        self.minimumUnsignedValue : Any = self.TEXTNOTSUPPORTED
#-------------------------------------------------------------------------------