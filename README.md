# pybridger
## Overview
    This is an ORM (object-relational mapping) using Python.
    You can manipulate databases as if you were manipulating objects, without having to write SQL directly.
    Supported SQL databases are sqlite3, MySQL, and PostgreSQL (ver:0.1.3).
## Features
    Unlike existing ORMs, it has the ability to import/export databases from CSV files.
    
## Installation
    pip install pybridger

## Usage
    <1, Engine definition>
    from pybridger import *

    engine = Engine(
        sqlEngineName = “mysql”,
        hostName      = “localhost”,
        userName      = “username”,
        password      = “password”,
        database      = “database”
    )
    engine.launch() 

    <2, Defining the table schema>
    class User(Model):
        id         = Column(Integer(), isPrimaryKey = True, isAutoIncrement= True)
        name       = Column(VarChar(50))
        email      = Column(VarChar(100))
        age        = Column(Integer())

    <3, Creating a Table>
    user = User.createTable()
    user.execute()
    user.commit()

    <4, Inserting data>
        user = User.insertRecord(id = 1, name = “name”, age = 19)
        user.execute()
        user.commit()

    <5, Updating data>
        user = User.updateRecord(name = “a”, age = 20)
        user.where(id = 1)
        user.execute()
        user.commit()

    <6, Deleting data>
        user = User.deleteRecord(id = 1) 
        user.execute()
        user.commit()
    
    <7, Retrieving data>
        user   = engine.select(User, User.id, User.name)
        result = user.where((User.age >= 20) & (User.age <= 29)).fetchall()


## File Structure  
    ...

## Author/Contact Information
    name  : KazuhiroKondo
    email : hkprr13@gmail.com

## Change History
    0.1.0 : 2025/08/14 : Initial version
    0.1.1 : 2025/08/14 : Minor fixes (FIled class)
    0.1.2 : 2025/08/16 : Mainly fixed CSV class and Engine class
    0.1.3 : 2025/08/25 : Reviewed overall structure and bug fixes
    0.1.4 : 2025/08/26 : Fix import error
    0.1.5 : 2025/08/26 : Add relation function and auto create table