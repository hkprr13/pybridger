#-------------------------------------------------------------------------------
from ...Base    import Base
#-------------------------------------------------------------------------------
class LeftJoin(Base):
    #--------------------------------------------------------------------------
    def __init__(
            self,
            tableName : str,
            columns   : str,
            joinTable : str,
            joinSql   : str,      
        ) -> None:
        super().__init__(tableName)
        self.query = f"SELECT {columns} FROM {tableName} "\
                   + f"LEFT JOIN {joinTable} ON {joinSql};"
#-------------------------------------------------------------------------------