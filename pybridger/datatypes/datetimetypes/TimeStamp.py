#-------------------------------------------------------------------------------
from typing         import Any                  # Any型
from .DateTimeType  import DateTimeType         # 日時型
from ...common      import override             # オーバライドデコレーター
from ...common      import private              # パブリックデコレーター
from ...query       import Query                # クエリクラス
#-------------------------------------------------------------------------------
class TimeStamp(DateTimeType):
    def __init__(
            self,
            precision  : int = 0,
            isTimeZone : bool = False
        ) -> None:
        super().__init__()
        self.__precision  = precision
        self.__isTimeZone = isTimeZone
    #---------------------------------------------------------------------------
    @private
    def __setFormat(self) -> str:
        __format = "YYYY-MM-DD HH:MM:SS"
        if self.__precision:
            return __format
        else:
            __format += "."
            __format += "f" * self.__precision
            return __format
    #---------------------------------------------------------------------------
    @private
    def __setPostgresqlQuery(self) -> Query:
        query = f"TIMESTAMP({self.__precision})"
        if self.__isTimeZone:
            query += "WITH TIME ZONE"
        return Query(query)
    #---------------------------------------------------------------------------
    @override
    def mysql(self) -> None:
        self.query  = Query(f"TIMESTAMP({self.__precision})")
        self.format = self.__setFormat()
        self.range  = "1970-01-01 00:00:01 UTC~2038-01-19 03:14:07 UTC"
    #---------------------------------------------------------------------------
    @override
    def sqlite3(self) -> None:
        self.query  = self.TEXTNOTSUPPORTED
        self.format = self.TEXTNOTSUPPORTED
        self.range  = self.TEXTNOTSUPPORTED
    #---------------------------------------------------------------------------
    @override
    def postgresql(self) -> None:
        self.query  = self.__setPostgresqlQuery()
        self.format = self.__setFormat()
        self.range  = "BC4713~AD294276"
#-------------------------------------------------------------------------------