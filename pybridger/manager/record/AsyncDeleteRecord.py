#-------------------------------------------------------------------------------
from ..AsyncBase import AsyncBase # 基底クラス
from ...common   import public    # パブリックメソッド
#-------------------------------------------------------------------------------
class AsyncDeleteRecord(AsyncBase):
    """
    レコード削除クラス
    """
    #---------------------------------------------------------------------------
    def __init__(
            self,
            tableName : str,
            columns   : str,
            values    : tuple
        ):
        """
        レコード削除のクラスの初期化
        """
        super().__init__(tableName)
        # クエリ
        query = f"DELETE FROM {self.tableName} WHERE {columns}"
        # プレイスホルダーをSQLによって置き換える
        self.query = query.replace(
            "?", self.sqlEngine.PLACEHOLDER
        )
        # 値
        self.values = values 
#-------------------------------------------------------------------------------