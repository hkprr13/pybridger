#-------------------------------------------------------------------------------
from ...Base    import Base
#-------------------------------------------------------------------------------
class FullOuterJoin(Base):
    #--------------------------------------------------------------------------
    def __init__(
            self,
            tableName : str,
            joinTable : str,
            joinSql   : str            
        ) -> None:
        super().__init__(tableName)
        self.query = f"SELECT * FROM {tableName} "\
                   + f"FULL OUTER JOIN {joinTable} ON {joinSql};"
#-------------------------------------------------------------------------------