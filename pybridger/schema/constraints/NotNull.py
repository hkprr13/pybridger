#-------------------------------------------------------------------------------
from .Constraints   import Constraints  # 基底クラス
from ...common      import override     # オーバライドデコレーター
from ...common      import private      # プライベートデコレーター
from ...common      import public       # パブリックデコレーター
from ...mapper      import Query        # クエリクラス
#-------------------------------------------------------------------------------
class NotNull(Constraints):
    """
    Defined not null constraints
    """
    #---------------------------------------------------------------------------
    def __init__(self):
        """
        Intialize not null constraints object
        """
    #---------------------------------------------------------------------------
    @override
    def mysql(self) -> None:
        self.query  = Query("NOT NULL")
    #---------------------------------------------------------------------------
    @override
    def sqlite3(self) -> None:
        self.query  = Query("NOT NULL")
    #---------------------------------------------------------------------------
    @override
    def postgresql(self) -> None:
        self.query  = Query("NOT NULL")
#-------------------------------------------------------------------------------
