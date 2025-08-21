#-------------------------------------------------------------------------------
from .Constraint    import Constraint  # 基底クラス
from ...common      import override     # オーバライドデコレーター
from ...mapper      import Query        # クエリクラス
#-------------------------------------------------------------------------------
class AutoIncrement(Constraint):
    """
    Defined auto increment constraint class
    """
    #---------------------------------------------------------------------------
    def __init__(self) -> None:
        super().__init__()
        """
        Initialize auto increment constraint object
        """
    #---------------------------------------------------------------------------
    @override
    def mysql(self) -> None:
        self.query  = Query(f"AUTO_INCREMENT")
    #---------------------------------------------------------------------------
    @override
    def sqlite3(self) -> None:
        self.query  = Query(f"AUTOINCREMENT")
    #---------------------------------------------------------------------------
    @override
    def postgresql(self) -> None:
        self.query  = Query(f"SERIAL")
#-------------------------------------------------------------------------------