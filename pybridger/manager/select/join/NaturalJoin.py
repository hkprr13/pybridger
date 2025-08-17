#-------------------------------------------------------------------------------
from ...Base    import Base
from ....common import public
#-------------------------------------------------------------------------------
class NaturalJoin(Base):
    #--------------------------------------------------------------------------
    def __init__(
            self,
            tableName : str,
            columns   : str,
            joinTable : str,
        ):
        super().__init__(tableName)
        self.query = f"SELECT {columns} FROM {tableName} "\
                   + f"NATURAL JOIN {joinTable};"
#-------------------------------------------------------------------------------