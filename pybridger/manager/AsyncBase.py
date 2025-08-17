#-------------------------------------------------------------------------------
from ..common   import public  # パブリックメソッド
from ..config   import Config  # コンフィグクラス
from ..query    import Query   # クエリクラス
#-------------------------------------------------------------------------------
class AsyncBase:
    """
    データベース操作マネージャークラスにおける基底クラス
    """
    def __init__(self, tableName : str):
        """初期化"""
        self.tableName = tableName
        self.query : str
        self.value : tuple
        self.data  : list[tuple[str]]
    #---------------------------------------------------------------------------
    @property
    @public
    def sqlEngine(self):
        """sqlエンジンの設定"""
        engine = Config.asyncSqlEngine
        if engine is None:
            raise Exception("エンジンが未設定です")
        return engine
    #---------------------------------------------------------------------------
    @public
    async def connect(self):
        """コネクト"""
        await self.sqlEngine.connect()
    #---------------------------------------------------------------------------        
    @public
    async def cursor(self):
        """カーソル"""
        return await self.sqlEngine.cursor()
    # #---------------------------------------------------------------------------
    @public
    async def execute(self):
        """クエリの実行"""
        await self.sqlEngine.execute(Query(self.query), self.value)
    #---------------------------------------------------------------------------
    @public
    async def executeAny(self):
        """複数クエリの実行"""
        await self.sqlEngine.executeAny(Query(self.query), self.data)
    #---------------------------------------------------------------------------
    @public
    async def commit(self):
        """データベースにコミットする"""
        await self.sqlEngine.commit()
    #---------------------------------------------------------------------------
    @public
    async def transaction(self):
        """トランザクション"""
        await self.sqlEngine.transaction()
    #---------------------------------------------------------------------------
    @public
    async def rollback(self):
        """ロールバック"""
        await self.sqlEngine.rollback()
#-------------------------------------------------------------------------------