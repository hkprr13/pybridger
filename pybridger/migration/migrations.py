#-------------------------------------------------------------------------------
from ..model        import Model
from ..column       import Column
from ..datatypes    import Integer
from ..datatypes    import VarChar
from ..datatypes    import TimeStamp
from ..datatypes    import Boolean
from ..constraints  import NotNull
from ..constraints  import Unique
from ..constraints  import Default
#-------------------------------------------------------------------------------
class migrations(Model):
    id = Column(
        dataType        = Integer(),
        isPrimaryKey    = True, 
        isAutoIncrement = True
    )
    name = Column(
        dataType = VarChar(255),
        notNull  = NotNull(True),
        unique   = Unique(True)
    )
    applied_at = Column(
        dataType = TimeStamp(),
        notNull  = NotNull(True)
    )
    checksum = Column(
        dataType = VarChar(255),
        notNull  = NotNull(True)
    )
    batch = Column(
        dataType = Integer(),
        notNull  = NotNull(True)
    )
    success = Column(
        dataType = Boolean(),
        notNull  = NotNull(True),
        default  = Default(1)
    )
#-------------------------------------------------------------------------------