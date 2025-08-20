#-------------------------------------------------------------------------------
from typing         import Any                  # Any型
from .DateTimeType  import DateTimeType         # 日時型
from ...common      import override             # オーバライドデコレーター
from ...common      import private              # パブリックデコレーター
from ...query       import Query                # クエリクラス
#-------------------------------------------------------------------------------
class Date(DateTimeType):
    """
    日付型
    サポートされているSQL(MySQL, PostgreSQL)
    """
    #---------------------------------------------------------------------------
    @override
    def mysql(self) -> None:
        self.query  = Query("DATE")
        self.format = "YYYY-MM-DD"
        self.range  = "1000-01-01~9999-12-31"
    #---------------------------------------------------------------------------
    @override
    def sqlite3(self) -> None:
        self.query  = self.TEXTNOTSUPPORTED
        self.format = self.TEXTNOTSUPPORTED
        self.range  = self.TEXTNOTSUPPORTED
    #---------------------------------------------------------------------------
    @override
    def postgresql(self) -> None:
        self.query  = Query("DATE")
        self.format = "YYYY-MM-DD"
        self.range  = "BC4713~AD5874897"
#-------------------------------------------------------------------------------