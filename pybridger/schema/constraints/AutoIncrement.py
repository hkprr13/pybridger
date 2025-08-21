#-------------------------------------------------------------------------------
from .Constraints   import Constraints  # 基底クラス
from ...common      import override     # オーバライドデコレーター
from ...mapper      import Query        # クエリクラス
#-------------------------------------------------------------------------------
class AutoIncrement(Constraints):
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