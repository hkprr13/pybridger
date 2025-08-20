#-------------------------------------------------------------------------------
from typing         import Any                  # Any型
from .StringsType   import StringsType          # 整数型
from ...common      import override             # オーバライドデコレーター
from ...common      import private              # パブリックデコレーター
from ...query       import Query                # クエリクラス
#-------------------------------------------------------------------------------
class Char(StringsType):
    """
    固定長の文字列データ型
    サポートされているSQL(すべて)
    """
    #---------------------------------------------------------------------------
    def __init__(self, length : int) -> None:
        super().__init__()
        self.length = length
    #---------------------------------------------------------------------------
    @override
    @private
    def mysql(self):
        self.query : Any = Query(f"CHAR({self.length})")
    #---------------------------------------------------------------------------
    @override
    @private
    def sqlite3(self):
        self.query : Any = Query(f"CHAR({self.length})")
    #---------------------------------------------------------------------------
    @override
    @private
    def postgresql(self):
        self.query : Any = Query(f"CHAR({self.length})")
#-------------------------------------------------------------------------------