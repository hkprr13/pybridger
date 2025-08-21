#-------------------------------------------------------------------------------
from .Constraints   import Constraints  # 基底クラス
from ...common      import override     # オーバライドデコレーター
from ...common      import private      # プライベートデコレーター
from ...mapper      import Query        # クエリクラス
#-------------------------------------------------------------------------------
class Unique(Constraints):
    """
    Defined unique constraints
    """
    def __init__(self):
        """
        Initialize unique constraints object
        """
    #---------------------------------------------------------------------------
    @override
    def mysql(self) -> None:
        self.query  = Query("UNIQUE")
    #---------------------------------------------------------------------------
    @override
    def sqlite3(self) -> None:
        self.query  = Query("UNIQUE")
    #---------------------------------------------------------------------------
    @override
    def postgresql(self) -> None:
        self.query  = Query("UNIQUE")
#-------------------------------------------------------------------------------
