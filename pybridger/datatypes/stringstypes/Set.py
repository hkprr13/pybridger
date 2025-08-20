#-------------------------------------------------------------------------------
from typing         import Any                  # Any型
from .StringsType   import StringsType          # 整数型
from ...common      import override             # オーバライドデコレーター
from ...common      import private              # パブリックデコレーター
from ...query       import Query                # クエリクラス
#-------------------------------------------------------------------------------
class Set(StringsType):
    """
    複数選択型
    サポートされているSQL(MySQL)
    """
    #---------------------------------------------------------------------------
    def __init__(self, *args) -> None:
        super().__init__()
        self.__args = args
    #---------------------------------------------------------------------------
    @override
    @private
    def mysql(self):
        self.query : Any = Query(f"SET{self.__args}")
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