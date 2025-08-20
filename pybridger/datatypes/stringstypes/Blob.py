#-------------------------------------------------------------------------------
from typing         import Any                  # Any型
from .StringsType   import StringsType          # 整数型
from ...common      import override             # オーバライドデコレーター
from ...common      import private              # パブリックデコレーター
from ...query       import Query                # クエリクラス
#-------------------------------------------------------------------------------
class Blob(StringsType):
    """
    大きなバイナリ型
    サポートされているSQL(MySQL, Sqlite3)
    """
    #---------------------------------------------------------------------------
    @override
    @private
    def mysql(self):
        self.query : Any = Query("BLOB")
    #---------------------------------------------------------------------------
    @override
    @private
    def sqlite3(self):
        self.query  : Any = Query("BLOB")
    #---------------------------------------------------------------------------
    @override
    @private
    def postgresql(self):
        self.query  : Any = self.TEXTNOTSUPPORTED
#-------------------------------------------------------------------------------