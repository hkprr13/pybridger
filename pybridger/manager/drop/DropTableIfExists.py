#-------------------------------------------------------------------------------
from ..Base     import Base   # 基底クラス
from ...common  import private # プライベートメソッド
from ...config  import Config
#-------------------------------------------------------------------------------
class DropTableIfExists(Base):
    """テーブル削除クラス"""
    def __init__(self, tableName: str):
        """
        テーブル削除クラスの初期化
        Args:
            tableName (str) : テーブル名
        """
        super().__init__(tableName)
        self.query = self.__buildQuery()
    #---------------------------------------------------------------------------
    @private
    def __buildQuery(self) -> str:
        """
        クエリの構築
        Returns:
            クエリ文字列
        Raises:
            Exceptin : エンジン未設定の場合
        """
        if self.sqlEngine == Config.sqlite3Engine:
            return f"DROP TABLE IF NOT EXISTS {self.tableName}"
        elif self.sqlEngine == Config.MySqlEngine:
            return f"DROP TABLE IF NOT EXISTS {self.tableName}"
        else:
            raise Exception("エンジン未設定です")
#-------------------------------------------------------------------------------