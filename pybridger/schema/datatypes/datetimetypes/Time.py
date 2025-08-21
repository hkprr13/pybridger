#-------------------------------------------------------------------------------
from .DateTimeType      import DateTimeType
from ....common         import override
from ....common         import private
from ....mapper         import Query
#-------------------------------------------------------------------------------
class Time(DateTimeType):
    """
    Time type
    Supported SQL (MySQL, PostgreSQL)
    """
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
        __format = "HH:MM:SS"
        if self.__precision:
            return __format
        else:
            __format += "."
            __format += "f" * self.__precision
            return __format
    #---------------------------------------------------------------------------
    @private
    def __setPostgresqlQuery(self) -> Query:
        query = f"TIME({self.__precision})"
        if self.__isTimeZone:
            query += "WITH TIME ZONE"
        return Query(query)
    #---------------------------------------------------------------------------
    @override
    @private
    def mysql(self) -> None:
        self.query  = Query(f"TIME({self.__precision})")
        self.format = self.__setFormat()
        self.range  = "-838:59:59~838:59:59"
    #---------------------------------------------------------------------------
    @override
    @private
    def sqlite3(self) -> None:
        self.query  = self.TEXTNOTSUPPORTED
        self.format = self.TEXTNOTSUPPORTED
        self.range  = self.TEXTNOTSUPPORTED
    #---------------------------------------------------------------------------
    @override
    @private
    def postgresql(self) -> None:
        self.query  = self.__setPostgresqlQuery()
        self.format = self.__setFormat()
        self.range  = "00:00:00~24:00:00"
#-------------------------------------------------------------------------------