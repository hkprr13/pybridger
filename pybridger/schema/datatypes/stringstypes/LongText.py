#-------------------------------------------------------------------------------
from typing         import Any                  # Any型
from .StringsType   import StringsType          # 整数型
from ...common      import override             # オーバライドデコレーター
from ...common      import private              # パブリックデコレーター
from ...query       import Query                # クエリクラス
#-------------------------------------------------------------------------------
class LongText(StringsType):
    """
    長程度のText型
    サポートされているSQL(MySQL)
    """
    #---------------------------------------------------------------------------
    @override
    @private
    def mysql(self):
        self.query : Any = Query("LONGTEXT")
    #---------------------------------------------------------------------------
    @override
    @private
    def sqlite3(self):
        self.query : Any = self.TEXTNOTSUPPORTED
    #---------------------------------------------------------------------------
    @override
    @private
    def postgresql(self):
        self.query : Any = self.TEXTNOTSUPPORTED
#-------------------------------------------------------------------------------