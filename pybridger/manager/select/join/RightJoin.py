#-------------------------------------------------------------------------------
from ...Base    import Base
from ....common import public
#-------------------------------------------------------------------------------
class RightJoin(Base):
    #--------------------------------------------------------------------------
    def __init__(
            self,
            tableName : str,
            columns   : str,
            joinTable : str,
            joinSql   : str,
            
        ):
        super().__init__(tableName)
        self.query = f"SELECT {columns} FROM {tableName} "\
                   + f"RIGHT JOIN {joinTable} ON {joinSql};"
#------------------------------------------------------------------------------