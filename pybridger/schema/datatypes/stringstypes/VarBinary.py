#-------------------------------------------------------------------------------
from typing         import Any                  # Any型
from .StringsType   import StringsType          # 整数型
from ...common      import override             # オーバライドデコレーター
from ...common      import private              # パブリックデコレーター
from ...query       import Query                # クエリクラス
#-------------------------------------------------------------------------------
class VarBinary(StringsType):
    """
    可変長バイナリデータ型
    サポートされているSQL(MySQL)
    """
    #---------------------------------------------------------------------------
    def __init__(self, length : int) -> None:
        super().__init__()
        self.length = length
    #---------------------------------------------------------------------------
    @override
    @private
    def mysql(self):
        self.query : Any = Query(f"VARBINARY({self.length})")
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