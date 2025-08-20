#-------------------------------------------------------------------------------
from typing         import Any                  # Any型
from .DateTimeType  import DateTimeType         # 日時型
from ...common      import override             # オーバライドデコレーター
from ...common      import private              # パブリックデコレーター
from ...query       import Query                # クエリクラス
#-------------------------------------------------------------------------------
class Year(DateTimeType):
    #---------------------------------------------------------------------------
    @override
    def mysql(self) -> None:
        self.query  = Query(f"YEAR")
        self.format = "YYYY"
        self.range  = "1901~2155"
    #---------------------------------------------------------------------------
    @override
    def sqlite3(self) -> None:
        self.query  = self.TEXTNOTSUPPORTED
        self.format = self.TEXTNOTSUPPORTED
        self.range  = self.TEXTNOTSUPPORTED
    #---------------------------------------------------------------------------
    @override
    def postgresql(self) -> None:
        self.query  = self.TEXTNOTSUPPORTED
        self.format = self.TEXTNOTSUPPORTED
        self.range  = self.TEXTNOTSUPPORTED
#-------------------------------------------------------------------------------