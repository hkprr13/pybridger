#-------------------------------------------------------------------------------
from typing         import Any                  # Any型
from .DateTimeType  import DateTimeType         # 日時型
from ...common      import override             # オーバライドデコレーター
from ...common      import private              # パブリックデコレーター
from ...query       import Query                # クエリクラス
#-------------------------------------------------------------------------------
class DateTime(DateTimeType):
    def __init__(self, precision : int = 0) -> None:
        super().__init__()
        self.precision = precision
    #---------------------------------------------------------------------------
    @private
    def __setMysqlFormat(self):
        __format = "YYYY-MM-DD HH:MM:SS"
        if self.precision:
            return __format
        else:
            __format += "."
            __format += "f" * self.precision
            return __format
    #---------------------------------------------------------------------------
    @override
    def mysql(self) -> None:
        self.query  = Query(f"DATETIME({self.precision})")
        self.format = self.__setMysqlFormat()
        self.range  = "1000-01-01 00:00:00~9999-12-31 23:59:59"
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