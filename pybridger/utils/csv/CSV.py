#-------------------------------------------------------------------------------
import csv
from typing         import cast
from typing         import Any

from pybridger.pybridger.mapper import Query


from ...engine      import Sqlite3Engine
from ...engine      import MySqlEngine
from ...engine      import PostgreSqlEngine
from ...common      import public
from ...common      import private
from ...config      import Config
from ...model       import Model
from ...errors      import EngineUndefinedError
from ...errors      import DatabaseUndefinedError
#-------------------------------------------------------------------------------
class CSV:
    """
    Define a class for importing/exporting CSV files to/from a database
    """
    #---------------------------------------------------------------------------
    def __init__(self) -> None:
        ...
    #---------------------------------------------------------------------------
    @property
    @public
    def __sqlEngine(self) -> Sqlite3Engine | MySqlEngine | PostgreSqlEngine:
        """
        Setting SQL engine
        Returns:
             Sqlite3Engine | MySqlEngine | PostgreSqlEngine : engine object
        """
        engine = Config.sqlEngine
        if engine is None:
            raise EngineUndefinedError()
        return engine
    #---------------------------------------------------------------------------
    @property
    @public
    def database(self) -> str:
        """
        Setting SQL database
        Returns:
            str : database name
        """
        database = Config.database
        if database is None:
            raise DatabaseUndefinedError
        return database
    #---------------------------------------------------------------------------
    @public
    def createTable(
            self,
            inputFilePath  : str,
            outputFilePath : str
        ) -> None:
        """
        Create a table from a CSV file

        Args:
            inputFilePath  (str): input .csv file
            outputFilePath (str): output .py file
        Examples:
            ```
            # Template table
            |User           |    |    |      |     |       |          |
            -----------------------------------------------------------
            |datetype       |    |    |      |     |       |          |
            |primarykey     |    |    |      |     |       |          |
            |autoincrement  |    |    |      |     |       |          |
            |default        |    |    |      |     |       |          |
            |notNull        |    |    |      |     |       |          |
            |unique         |    |    |      |     |       |          |
            |check          |    |    |      |     |       |          |
            |tableLevelCheck|    |    |      |     |       |          |
            |foreignkey     |    |    |      |     |       |          |
            # Entered table
            |User           |id  |name|age   |email|address|created_at|
            -----------------------------------------------------------
            |datetype       |int |str |int   |str  |str    |datetime  |
            |primarykey     |TRUE|    |      |     |       |          |
            |autoincrement  |TRUE|    |      |     |       |          |
            |default        |    |    |      |     |       |          |
            |notNull        |    |TRUE|TRUE  |TRUE |TRUE   |          |
            |unique         |    |    |      |     |       |          |
            |check          |    |    |age>=0|     |       |          |
            |tableLevelCheck|    |    |      |     |       |          |
            |foreignkey     |    |    |      |     |       |          |
            
            # CSV file to be included as an argument
            # Input csv file(.csv)
            User,id,name ,age,email,address,created_at
            datetype,int,str,int,str,str,datetime
            primarykey,TRUE,,,,,
            autoincrement,TRUE,,,,,
            default,,,,,,
            notNull,,TRUE,TRUE,TRUE,TRUE,
            unique,,,,,,
            check,,,age>=0,,,
            tableLevelCheck,,,,,,
            foreignkey,,,,,,
            # Creation schema
                # Table
                name = User
                # Columns
                id        INTEGER  PRIMARY KEY AUTOINCREMAENT
                name      TEXT     NOTNULL
                age       INTEGER  NOTNULL CHECK(age>=0)
                email     TEXT     NOTNULL 
                address   TEXT     NOTNULL 
                create_at DATETIME
            # Output file (.py) result
            #---------------------------------------------------------------------------
            from pybridger import *

            engine = Engine() # Set the arguments

            # Table definition
            class User(Model):
                id        = Column(dataType = Integer(), isPrimaryKey = True, isAutoIncrement = True)
                name      = Column(dataType = Text, iNotNull = True)
                age       = Column(dataType = Integer(), iNotNull = True, check = CHECK(age>=0))
                email     = Column(dataType = Text, iNotNull = True)
                create_at = Column(dataType = DateTime, iNotNull = True)
            #---------------------------------------------------------------------------
            ```

        """
        tableName, columnDefines = self.__makeColumnDefines(inputFilePath)
        with open(
            outputFilePath, mode = "w", newline = "", encoding = "utf-8"
        ) as f:
            w = f.write
            w("#---------------------------------------------------------------------------")
            w(f"from pybridger import *\n")
            w(f"\n")
            w(f"engine = Engine() # Set the arguments\n")
            w(f"engine.launch()\n")
            w(f"\n")
            w("# Table definition\n")
            w(f"class {tableName}(Model):\n    ")
            line = self.__makeColumnLinesOfTable(columnDefines)
            w(line[:-4])
            w("#---------------------------------------------------------------------------")
    #---------------------------------------------------------------------------
    @private
    def __makeColumnLinesOfTable(self, columnDefines : list[str]) -> str:
        line = ""
        for col in columnDefines:
            l = f"{col[0]} = Column(dataType = "
            dataType = col[1]
            if dataType == "int":
                l += "Integer(), "
            elif dataType == "str":
                l += "Text(), "
            elif dataType == "bool":
                l += "Boolean(), "
            elif dataType == "float":
                l += "Float(), "
            elif dataType == "datetime":
                l += "DateTime(), "
            elif dataType == "time":
                l += "Time(), "
            primaryKey = col[2]
            if primaryKey.lower() == "true":
                l += "isPrimaryKey = True, "
            elif primaryKey.lower() == "false":
                l += "isPrimaryKey = False, "
            autoIncrement = col[3]
            if autoIncrement.lower() == "true":
                l += "isAutoIncrement = True, "
            elif autoIncrement.lower() == "false":
                l += "isAutoIncrement = False, "
            default = col[4]
            if default:
                l += f"Defalut('{default}'), "
            notNull = col[5]
            if notNull.lower() == "true":
                l += "notNull = NotNull(True), "
            elif notNull.lower() == "false":
                l += "notNull = NotNull(False), "
            unique = col[6]
            if unique.lower() == "true":
                l += "unique = Unique(True), "
            elif unique.lower() == "false":
                l += "unique = Unique(False), "
            check = col[7]
            if check:
                l += f"check = Check('{check}'), "                      
            tableLevelCheck = col[8]
            if tableLevelCheck:
                l += f"tableLevelCheck = TableLevelCheck('{tableLevelCheck}'), "       
            foreignKey = col[9]
            if foreignKey:
                l += f"foreignKey = ForeignKey('{foreignKey}'), "
            l = l[:-2] + ") \n    "
            line += l
        return line
    #---------------------------------------------------------------------------
    @private
    def __makeColumnDefines(
            self, filePath : str
        ) -> tuple[str, list[str]]:
        with open(filePath, mode = "r", newline = "", encoding = "utf-8") as f:
            # Getting the first line
            headerLine : str = f.readline().strip()
            # List the first row (set column)
            columns : list = headerLine.split(",")
            # Get the table name (location 0,0 in csv)
            # and set columns to columns only
            tableName : str  = columns.pop(0)
            # Define column
            columnDefines = [columns]
            for line in f.readlines():
                lines :str = line.strip()
                lineParts : list = lines.split(",")
                columnDefines.append(lineParts[1:])
            cols = []
            # Reverse order
            for i in (map(list, zip(*columnDefines))):
                cols.append(i)
            return tableName, cols
    #---------------------------------------------------------------------------
    @public
    def importToDatabase(self, filePath : str, model : type[Model]):
        """
        Import CSV files into the database
        """
        # Reading and separating CSV files
        self.__tableName = model.tableName
        header, data = self.__parseCSV(filePath)
        # Matching DB columns
        dbColumns = self.__getTableColumns()
        if not set(header) == set(dbColumns):
            raise Exception(
                "The headers in the CSV file"
                "do not match the columns in the database"
            )
        # placeholder
        placeHolders = "(" \
                     + ", ".join([self.__sqlEngine.PLACEHOLDER * len(header)]) \
                     + ")"
        columnsSql = "(" \
                   + ", ".join([f"{col}" for col in header]) \
                   + ")"
        query = f"INSERT INTO {self.__tableName} " \
              + f"{columnsSql} VALUES {placeHolders}"
        try:
            self.__sqlEngine.executeAny(Query(query), data)
            self.__sqlEngine.commit()
        except Exception as e:
            self.__sqlEngine.rollback()
            raise Exception(f"Data insertion failed: {e}")
    #---------------------------------------------------------------------------
    @public
    def exportFromDatabase(self,  filePath : str, model : type[Model]) -> None:
        """
        Exporting a database to a CSV file
        """
        self.__tableName = model.tableName
        query = f"SELECT * FROM {self.__tableName};"
        cur = self.__sqlEngine.cursor()
        cur.execute(query)
        data = cur.fetchall()
        # Writing CSV
        with open(filePath, mode = "w", newline = "", encoding = "utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(self.__getTableColumns())
            writer.writerows(data)
        print(f"Created {filePath}")
    #---------------------------------------------------------------------------
    @private
    def __parseCSV(self, filePath : str) -> tuple[list[str], list[tuple]]:
        try:
            with open(filePath, newline = "", encoding= "utf-8") as csvFile:
                reader = csv.reader(csvFile)
                header = next(reader)
                if not header:
                    raise ValueError(
                        "There is no header in the CSV file"
                    )
                data = []
                for row in reader:
                    if not len(row) == len(header):
                        raise ValueError(
                            "The number of rows in the CSV file"
                            "does not match the number of columns in the header"
                        )
                    data.append(tuple(row))
                return header, data
        except FileNotFoundError:
            raise FileNotFoundError(
                "CSV file does not exist"
            )
        except StopIteration:
            raise ValueError(
                "The CSV file is empty"
            )
        except Exception as e:
            raise Exception(
                f"Failed to load CSV file: {e}"
            )
    #---------------------------------------------------------------------------
    @private
    def __getTableColumns(self) -> list[Any]:
        if isinstance(self.__sqlEngine, MySqlEngine):
            query = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS " \
                  + f"WHERE TABLE_SCHEMA = {self.__sqlEngine.PLACEHOLDER}" \
                  + f"AND TABLE_NAME = {self.__sqlEngine.PLACEHOLDER};"
            cur = self.__sqlEngine.cursor()
            cur.execute(query, (self.database, self.__tableName))
            rows = cast(list[dict[str, Any]], cur.fetchall())
            return [row["COLUMN_NAME"] for row in rows]
        elif isinstance(self.__sqlEngine, Sqlite3Engine):
            query = f"PRAGMA table_info({self.__tableName});"
            cur = self.__sqlEngine.cursor()
            cur.execute(query)
            return [row[1] for row in cur.fetchall()]
        else:
            raise EngineUndefinedError()
#-------------------------------------------------------------------------------
