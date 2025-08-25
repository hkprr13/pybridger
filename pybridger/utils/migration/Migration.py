#-------------------------------------------------------------------------------
import os
import sys
import re
import hashlib
import importlib.util
from datetime       import datetime
from pathlib        import Path
from ...engine      import Engine
from ...common      import private
from ...config      import Config
from ...mapper      import Query
#-------------------------------------------------------------------------------
class Migration:
    def __init__(
            self,
            engine        : Engine,
            migrationsDir : str
        ) -> None:
        """
        マイグレーションクラスの初期化
        Args:
            migrationsDir (str) : マイグレーションディレクトリのパス
        """
        super().__init__()
        self.__migrationsDir = Path(migrationsDir)
        self.__migrationsDir.mkdir(exist_ok = True)
        # テーブルの作成
        self.tableName = ""
        #
        # 未実装
        #
        #
        print("初期化完了")
    #---------------------------------------------------------------------------
    @property
    @private
    def __sqlEngine(self):
        """
        sqlエンジンの設定
        """
        engine = Config.sqlEngine
        if engine is None:
            raise Exception("エンジンが未設定です")
        return engine
    #---------------------------------------------------------------------------
    @private
    def __checksum(self, path : Path) -> str:
        h = hashlib.sha1()
        with open(path, "rb") as f:
            h.update(f.read())
        return h.hexdigest()
    #---------------------------------------------------------------------------
    @private
    def __discoverFiles(self):
        return sorted(self.__migrationsDir.glob("*.py"))
    #---------------------------------------------------------------------------
    @private
    def __applied(self):
        cur = self.__sqlEngine.cursor()
        cur.execute(
            f"SELECT name, check FROM {self.tableName} ORDER BY id"
        )
        rows = cur.fetchall()
        return {r[0] : r[1] for r in rows}
    #---------------------------------------------------------------------------
    @private
    def __loadModule(self,path : Path):
        spec = importlib.util.spec_from_file_location(path.stem, path)
        if not spec is None:
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return mod
        else:
            raise Exception()
    #---------------------------------------------------------------------------
    @private
    def __nextBatch(self) -> int:
        self.__sqlEngine.cursor()
        self.__sqlEngine.execute(
            Query(f"SELECT COALESCE(MAX(batch), 0) FROM {self.tableName}")
        )
        rows = self.__sqlEngine.fetchall()
        if not rows is None:
            (val, ) = rows
            return val
        else: 
            raise Exception()
    #---------------------------------------------------------------------------
    @property
    @private
    def __bulidHistoryQuery(self):
        return Query("SELECT name FROM migration ORDER BY id")
    #---------------------------------------------------------------------------
    def make(self, name : str) -> None:
        """
        新しいマイグレーションファイルを作成する
        Args:
            name (str) : マイグレーション名
        """
        timeStamp = datetime.now().strftime("%Y%m%d%H%M%S")
        fileName  = f"{timeStamp}_" \
                  + f"{re.sub(r'[^0-9A-Za-z_]+', '_', name.strip())}.py"
        filePath  = os.path.join(self.__migrationsDir, fileName)
        with open(filePath, "w", encoding = "utf-8") as f:
            w = f.write
            w("def upgrade(engine):\n")
            w("    # ここにスキーマ変更SQLを記述\n")
            w("    pass\n")
            w("def downgrade(engine):\n")
            w("    # 元に戻すSQLを記述\n")
            w("    pass")
        print(f"{filePath}を作成しました")
    #---------------------------------------------------------------------------
    def up(self, steps : int | None = None):
        applied = self.__applied()
        files   = self.__discoverFiles()
        pending = [f for f in files if f.stem not in applied]
        if steps:
            pending = pending[:steps]
        if not pending:
            return
        batch = self.__nextBatch()
        for f in pending:
            mod      = self.__loadModule(f)
            checksum = self.__checksum(f)
            try:
                ...
                #
                #
                #
                #
            except Exception as e:
                self.__sqlEngine.rollback()
                raise
    #---------------------------------------------------------------------------
    def history(self) -> list:
        """
        適用済みのマイグレーション一覧を返す
        Returns:
            list[str] : ファイル名のリスト
        """
        self.__sqlEngine.execute(self.__bulidHistoryQuery)
        rows = self.__sqlEngine.fetchall()
        if rows:
            return [r[0] for r in rows]
        else:
            return []
    
#-------------------------------------------------------------------------------