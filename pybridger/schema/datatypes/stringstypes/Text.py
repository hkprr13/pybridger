#-------------------------------------------------------------------------------
from typing         import Any                  # Any型
from .StringsType   import StringsType          # 整数型
from ...common      import override             # オーバライドデコレーター
from ...common      import private              # パブリックデコレーター
from ...query       import Query                # クエリクラス
#-------------------------------------------------------------------------------
class Text(StringsType):
    """
    Text型
    サポートされているSQL(すべて)
    """
    #---------------------------------------------------------------------------
    @override
    @private
    def mysql(self):
        self.query : Any = Query("TEXT")
    #---------------------------------------------------------------------------
    @override
    @private
    def sqlite3(self):
        self.query : Any = Query("TEXT")
    #---------------------------------------------------------------------------
    @override
    @private
    def postgresql(self):
        self.query : Any = Query("TEXT")
#-------------------------------------------------------------------------------