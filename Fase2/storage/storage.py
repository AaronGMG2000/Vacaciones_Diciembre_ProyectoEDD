# -------------------------------
# Released under MIT License
# Copyright (c) 2020 TytusDb Team 18

from .avl import avlMode as avl
from .b import BMode as b
from .bplus import BPlusMode as bplus
from .dict import DictMode as dict
from .hash import HashMode as hash
from .isam import ISAMMode as isam
from .json import jsonMode as json
from . import Serializable as Serializable
from . import blockchain as block
from . import Criptografia as crypt
import hashlib
import shutil
import os

#----------------Data--------------------#

def checkData():
    if not os.path.isdir("./Data"):
        os.mkdir("./Data")
    if not os.path.isfile("./Data/Data.bin"):
        dataBaseTree = {}
        Serializable.update('./Data', 'Data', dataBaseTree)
        Serializable.update('./Data', 'DataTables', dataBaseTree)
    if not os.path.isdir("./Data/security"):
        os.mkdir("./Data/security")
    if not os.path.isdir("./Data/hash"):
        hash.__init__()
        hash._storage = hash.ListaBaseDatos.ListaBaseDatos()
    if not os.path.isdir("./Data/B"):
        os.mkdir("./Data/B")
        b.b = b.db.DB()

def dropAll():
    dict.dropAll()
    hash.__init__()
    hash._storage = hash.ListaBaseDatos.ListaBaseDatos()
    b.b = b.db.DB()
#----------------DataBase----------------#

def createDatabase(database: str, mode: str, encoding: str) -> int:
    checkData()
    data = Serializable.Read('./Data/',"Data")
    if encoding not in ['ascii', 'iso-8859-1', 'utf8']:
        return 4
    if mode not in ['avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash']:
        return 3
    if not data.get(database):
        if mode == 'avl':
            res = avl.createDatabase(database)
        elif mode == 'b':
            res = b.createDatabase(database)
        elif mode == 'bplus':
            res = bplus.createDatabase(database)
        elif mode == 'dict':
            res = dict.createDatabase(database)
        elif mode == 'isam':
            res = isam.createDatabase(database)
        elif mode == 'json':
            res = json.createDatabase(database)
        elif mode == 'hash':
            res = hash.createDatabase(database)
        if not res:
            data[database] = [database,[mode],encoding]
            Serializable.update('./Data', 'Data', data)
        return res
    else:
        return 2

def showDatabases() -> list:
    checkData()
    data = Serializable.Read('./Data/',"Data")
    temp = []
    for x in list(data.values()):
        temp.append(x[0])
    return temp

def alterDatabase(databaseOld, databaseNew) -> int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(databaseOld)
        if db:
            if data.get(databaseNew):
                return 3
            mode =db[1][0] 
            if mode == 'avl':
                res = avl.alterDatabase(databaseOld, databaseNew)
            elif mode == 'b':
                res = b.alterDatabase(databaseOld, databaseNew)
            elif mode == 'bplus':
                res = bplus.alterDatabase(databaseOld, databaseNew)
            elif mode == 'dict':
                res = dict.alterDatabase(databaseOld, databaseNew)
            elif mode == 'isam':
                res = isam.alterDatabase(databaseOld, databaseNew)
            elif mode == 'json':
                res = json.alterDatabase(databaseOld, databaseNew)
            elif mode == 'hash':
                res = hash.alterDatabase(databaseOld, databaseNew)
            if not res:
                del data[databaseOld]
                db[0] = databaseNew
                data[databaseNew] = db
                Serializable.update('./Data', 'Data', data)
            return res
        else:
            return 2
    except:
        return 1

def dropDatabase(database: str) -> int: 
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            mode =db[1][0] 
            if 'avl' in db[1]:
                if mode == 'avl':
                    res = avl.dropDatabase(database)
                else:
                    avl.dropDatabase(database)
            if 'b' in db[1]:
                if mode == 'b':
                    res = b.dropDatabase(database)
                else:
                    b.dropDatabase(database)
            if 'bplus' in db[1]:
                if mode == 'bplus':
                    res = bplus.dropDatabase(database)
                else:
                    bplus.dropDatabase(database)
            if 'dict' in db[1]:
                if mode == 'dict':
                    res = dict.dropDatabase(database)
                else:
                    dict.dropDatabase(database)
            if 'isam' in db[1]:    
                if mode == 'isam':
                    res = isam.dropDatabase(database)
                else:
                    isam.dropDatabase(database)
            if 'json' in db[1]:
                if mode == 'json':
                    res = json.dropDatabase(database)
                else:
                    json.dropDatabase(database)
            if 'hash' in db[1]:
                if mode == 'hash':
                    res = hash.dropDatabase(database)
                else:
                    hash.dropDatabase(database)
            if not res:
                del data[database]
                Serializable.update('./Data', 'Data', data)
            return res
        else:
            return 2
    except:
        return 1

def alterDatabaseMode(database: str, mode: str) -> int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if mode not in ['avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash']:
            return 4
        if db:
            tablas = []
            mod =db[1][0]
            if mod== mode:
                return 0
            
            if mod == 'avl':
                tablas = avl.showTables(database)
                res = cambioTablas(avl, tablas, database, mode, db)
                if not res:
                    avl.dropDatabase(database)
            elif mod == 'b':
                tablas = b.showTables(database)
                res = cambioTablas(b, tablas, database, mode, db)
                if not res:
                    b.dropDatabase(database)
            elif mod == 'bplus':
                tablas = bplus.showTables(database)
                res = cambioTablas(bplus, tablas, database, mode, db)
                if not res:
                    bplus.dropDatabase(database)
            elif mod == 'dict':
                tablas = dict.showTables(database)
                res = cambioTablas(dict, tablas, database, mode, db)
                if not res:
                    dict.dropDatabase(database)
            elif mod == 'isam':
                tablas = isam.showTables(database)
                res = cambioTablas(isam, tablas, database, mode, db)
                if not res:
                    isam.dropDatabase(database)
            elif mod == 'json':
                tablas = json.showTables(database)
                res = cambioTablas(json, tablas, database, mode, db)
                if not res:
                    json.dropDatabase(database)
            elif mod == 'hash':
                tablas = hash.showTables(database)
                res = cambioTablas(hash, tablas, database, mode, db)
                if not res:
                    hash.dropDatabase(database)
            data[database] = db
            Serializable.update('./Data', 'Data', data)
            return res
        else:
            return 2
    except:
        return 1

def cambioTablas(modo, tablas, database, mode, db):
    checkData()
    if mode in db:
        db[1].pop(0)
        db[1].remove(mode)
        db[1].insert(0,mode)
    else:
        db[1].pop(0)
        db[1].insert(0,mode)
        if mode == 'avl':
            avl.createDatabase(database)
            mod = avl
        elif mode == 'b':
            b.createDatabase(database)
            mod = b
        elif mode == 'bplus':
            bplus.createDatabase(database)
            mod = bplus
        elif mode == 'dict':
            dict.createDatabase(database)
            mod = dict
        elif mode == 'isam':
            isam.createDatabase(database)
            mod = isam
        elif mode == 'json':
            json.createDatabase(database)
            mod = json
        elif mode == 'hash':
            hash.createDatabase(database)
            mod = hash
    
    import csv
    for x in tablas:
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+x)
        tab[1] = mode
        mod.createTable(database, x, tab[2])

        # for y in modo.extractTable(database, x):
        #     mod.insert(database, x,y)

        file = open("./data/change.csv", "w", newline='', encoding='utf-8')
        spamreader = csv.writer(file)
        
        for y in modo.extractTable(database, x):
            spamreader.writerow(y)
        file.close()
        if len(tab[3]):
            mod.alterAddPK(database, x, tab[3])
        mod.loadCSV("./data/change.csv", database, x)
        os.remove("./data/change.csv")
        Serializable.update('./Data', 'DataTables', dataTable)
    return 0

#----------------Table-------------------#

def createTable(database: str, table: str, numberColumns: int) -> int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        dataTable = Serializable.Read('./Data/',"DataTables")
        db = data.get(database)
        if db:
            mode =db[1][0] 
            if mode == 'avl':
                res = avl.createTable(database, table, numberColumns)
                dataTable[database+"_"+table] = [table, 'avl', numberColumns, []]
            elif mode == 'b':
                res = b.createTable(database, table, numberColumns)
                dataTable[database+"_"+table] = [table, 'b', numberColumns, []]
            elif mode == 'bplus':
                res = bplus.createTable(database, table, numberColumns)
                dataTable[database+"_"+table] = [table, 'bplus', numberColumns, []]
            elif mode == 'dict':
                res = dict.createTable(database, table, numberColumns)
                dataTable[database+"_"+table] = [table, 'dict', numberColumns, []]
            elif mode == 'isam':
                res = isam.createTable(database, table, numberColumns)
                dataTable[database+"_"+table] = [table, 'isam', numberColumns, []]
            elif mode == 'json':
                res = json.createTable(database, table, numberColumns)
                dataTable[database+"_"+table] = [table, 'json', numberColumns, []]
            elif mode == 'hash':
                res = hash.createTable(database, table, numberColumns)
                dataTable[database+"_"+table] = [table, 'hash', numberColumns, []]
            Serializable.update('./Data', 'DataTables', dataTable)
            return res
        else:
            return 2
    except:
        return 1

def showTables(database: str) -> list:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            res = []
            if 'avl' in db[1]:
                res = res + avl.showTables(database)
            if 'b' in db[1]:
                res = res + b.showTables(database)
            if 'bplus' in db[1]:
                res = res + bplus.showTables(database)
            if 'dict' in db[1]:
                res = res + dict.showTables(database)
            if 'isam' in db[1]:
                res = res + isam.showTables(database)
            if 'json' in db[1]:
                res = res + json.showTables(database)
            if 'hash' in db[1]:
                res = res + hash.showTables(database)
            return res
        else:
            return None
    except:
        return None

def extractTable(database: str, table: str) -> list:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                if tab[1] == 'avl':
                    res = avl.extractTable(database, table)
                elif tab[1] == 'b':
                    res = b.extractTable(database, table)
                elif tab[1] == 'bplus':
                    res = bplus.extractTable(database, table)
                elif tab[1] == 'dict':
                    res = dict.extractTable(database, table)
                elif tab[1] == 'isam':
                    res = isam.extractTable(database, table)
                elif tab[1] == 'json':
                    res = json.extractTable(database, table)
                elif tab[1] == 'hash':
                    res = hash.extractTable(database, table)
                return res
        return None
    except:
        return None

def extractRangeTable(database: str, table: str, columnNumber: int, 
                      lower: any, upper: any) -> list:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            res = None
            if 'avl' in db[1] and res == None:
                res = avl.extractRangeTable(database, table, columnNumber, lower, upper)
            if 'b' in db[1] and res == None:
                res = b.extractRangeTable(database, table, columnNumber, lower, upper)
            if 'bplus' in db[1] and res == None:
                res = bplus.extractRangeTable(database, table, columnNumber, lower, upper)
            if 'dict' in db[1] and res == None:
                res = dict.extractRangeTable(database, table, columnNumber, lower, upper)
            if 'isam' in db[1] and res == None:
                res = isam.extractRangeTable(database, table, columnNumber, lower, upper)
            if 'json' in db[1] and res == None:
                res = json.extractRangeTable(database, table, lower, upper)
            if 'hash' in db[1] and res == None:
                res = hash.extractRangeTable(database, table, columnNumber, lower, upper)
            return res
        else:
            return 2
    except:
        return 1


def alterAddPK(database: str, table: str, columns: list) -> int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        db = data.get(database)
        if db:
            if tab:
                if tab[1] == 'avl':
                    res = avl.alterAddPK(database, table, columns)
                elif tab[1] == 'b':
                    res = b.alterAddPK(database, table, columns)
                elif tab[1] == 'bplus':
                    res = bplus.alterAddPK(database, table, columns)
                elif tab[1] == 'dict':
                    res = dict.alterAddPK(database, table, columns)
                elif tab[1] == 'isam':
                    res = isam.alterAddPK(database, table, columns)
                elif tab[1] == 'json':
                    res = json.alterAddPK(database, table, columns)
                elif tab[1] == 'hash':
                    res = hash.alterAddPK(database, table, columns)
                if not res:
                    tab[3] = columns
                    Serializable.update('./Data', 'DataTables', dataTable)
                return res
            else:
                return 3
        else:
            return 2
    except:
        return 1


def alterDropPK(database: str, table: str) -> int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                if tab[1] == 'avl':
                    res = avl.alterDropPK(database, table)
                elif tab[1] == 'b':
                    res = b.alterDropPK(database, table)
                elif tab[1] == 'bplus':
                    res = bplus.alterDropPK(database, table)
                elif tab[1] == 'dict':
                    res = dict.alterDropPK(database, table)
                elif tab[1] == 'isam':
                    res = isam.alterDropPK(database, table)
                elif tab[1] == 'json':
                    res = json.alterDropPK(database, table)
                elif tab[1] == 'hash':
                    res = hash.alterDropPK(database, table)
                if not res:
                    tab[3] = []
                    Serializable.update('./Data', 'DataTables', dataTable)
                return res
            else:
                return 3
        else:
            return 2
    except:
        return 1


def alterTableAddFK(database: str, table: str, indexName: str, 
                    columns: list,  tableRef: str, columnsRef: list) -> int:
    pass

def alterTableDropFK(database: str, table: str, indexName: str) -> int:
    pass

def alterAddIndex(database: str, table: str, references: dict) -> int:
    pass

def alterTable(database: str, tableOld: str, tableNew: str) -> int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+tableOld)
        if db:
            if tab:
                if tab[1] == 'avl':
                    res = avl.alterTable(database, tableOld, tableNew)
                elif tab[1] == 'b':
                    res = b.alterTable(database, tableOld, tableNew)
                elif tab[1] == 'bplus':
                    res = bplus.alterTable(database, tableOld, tableNew)
                elif tab[1] == 'dict':
                    res = dict.alterTable(database, tableOld, tableNew)
                elif tab[1] == 'isam':
                    res = isam.alterTable(database, tableOld, tableNew)
                elif tab[1] == 'json':
                    res = json.alterTable(database, tableOld, tableNew)
                elif tab[1] == 'hash':
                    res = hash.alterTable(database, tableOld, tableNew)
                if not res:
                    del dataTable[database+"_"+tableOld]
                    tab[0]=tableNew
                    dataTable[database+"_"+tableNew] = tab
                    Serializable.update('./Data', 'DataTables', dataTable)
                return res
            else:
                return 3
        else:
            return 2
    except:
        return 1


def alterAddColumn(database: str, table: str, default: any) -> int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                if tab[1] == 'avl':
                    res = avl.alterAddColumn(database, table, default)
                elif tab[1] == 'b':
                    res = b.alterAddColumn(database, table, default)
                elif tab[1] == 'bplus':
                    res = bplus.alterAddColumn(database, table, default)
                elif tab[1] == 'dict':
                    res = dict.alterAddColumn(database, table, default)
                elif tab[1] == 'isam':
                    res = isam.alterAddColumn(database, table, default)
                elif tab[1] == 'json':
                    res = json.alterAddColumn(database, table, default)
                elif tab[1] == 'hash':
                    res = hash.alterAddColumn(database, table, default)
                if not res:
                    tab[2]+=1
                    Serializable.update('./Data', 'DataTables', dataTable)
                return res
            else:
                return 3
        else:
            return 2
    except:
        return 1


def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                if tab[1] == 'avl':
                    res = avl.alterDropColumn(database, table, columnNumber)
                elif tab[1] == 'b':
                    res = b.alterDropColumn(database, table, columnNumber)
                elif tab[1] == 'bplus':
                    res = bplus.alterDropColumn(database, table, columnNumber)
                elif tab[1] == 'dict':
                    res = dict.alterDropColumn(database, table, columnNumber)
                elif tab[1] == 'isam':
                    res = isam.alterDropColumn(database, table, columnNumber)
                elif tab[1] == 'json':
                    res = json.alterDropColumn(database, table, columnNumber)
                elif tab[1] == 'hash':
                    res = hash.alterDropColumn(database, table, columnNumber)
                if not res:
                        tab[2]+=1
                        Serializable.update('./Data', 'DataTables', dataTable)
                return res
            else:
                return 3
        else:
            return 2
    except:
        return 1

def dropTable(database: str, table: str) -> int: 
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                mod = None
                if tab[1] == 'avl':
                    res = avl.dropTable(database, table)
                    mod = avl
                elif tab[1] == 'b':
                    res = b.dropTable(database, table)
                    mod = b
                elif tab[1] == 'bplus':
                    res = bplus.dropTable(database, table)
                    mod = bplus
                elif tab[1] == 'dict':
                    res = dict.dropTable(database, table)
                    mod = dict
                elif tab[1] == 'isam':
                    res = isam.dropTable(database, table)
                    mod = isam
                elif tab[1] == 'json':
                    res = json.dropTable(database, table)
                    mod = json
                elif tab[1] == 'hash':
                    res = hash.dropTable(database, table)
                    mod = hash
                if not res:
                    if not len(mod.showTables(database)) and db[1][0]!=tab[1]:
                        mod.dropDatabase(database)
                        db[1].remove(tab[1])
                    data[database] = db
                    del dataTable[database+"_"+table]
                    Serializable.update('./Data', 'Data', data)
                    Serializable.update('./Data', 'DataTables', dataTable)
                return res
            else:
                return 3
        else:
            return 2
    except:
        return 1

def alterTableMode(database: str, table: str, mode: str) -> int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if mode not in ['avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash']:
            return 4
        if db:
            if not tab:
                return 3
            if mode == tab[1]:
                    return 4
            tuplas = None
            if mode not in db[1]:
                db[1].append(mode)

            if  tab[1] == 'avl':
                tuplas = avl.extractTable(database, table)
                modo = avl
                avl.dropTable(database, table)

            elif  tab[1] == 'b':
                tuplas = b.extractTable(database, table)
                b.dropTable(database, table)
                modo = b

            elif  tab[1] == 'bplus':
                tuplas = bplus.extractTable(database, table)
                bplus.dropTable(database, table)
                modo = bplus

            elif  tab[1] == 'dict':
                tuplas = dict.extractTable(database, table)
                dict.dropTable(database, table)
                modo = dict

            elif  tab[1] == 'isam':
                tuplas = isam.extractTable(database, table)
                isam.dropTable(database, table)
                modo = isam

            elif  tab[1] == 'json':
                tuplas = json.extractTable(database, table)
                json.dropTable(database, table)
                modo = json

            elif  tab[1] == 'hash':
                tuplas = hash.extractTable(database, table)
                hash.dropTable(database, table)
                modo = hash

            if tab[1] != db[1][0] and tuplas!=None:
                if not len(modo.showTables(database)):
                    modo.dropDatabase(database)
                    db[1].remove(tab[1])

            if tuplas!=None:
                if mode == 'avl':
                    mod = avl
                elif mode == 'b':
                    mod = b
                elif mode == 'bplus':
                    mod = bplus
                elif mode == 'isam':
                    mod = isam
                elif mode == 'dict':
                    mod = dict
                elif mode == 'json':
                    mod = json
                elif mode == 'hash':
                    mod = hash
                import csv
                file = open("./data/change.csv", "w", newline='', encoding='utf-8')
                spamreader = csv.writer(file)
                t=0
                if mod.showTables(database) == None:
                    mod.createDatabase(database)
                for y in tuplas:
                    if t == 0:
                        mod.createTable(database, table, len(y))
                    spamreader.writerow(y)
                    t=1
                file.close()
                if len(tab[3]):
                    mod.alterAddPK(database, table, tab[3])
                mod.loadCSV("./data/change.csv", database, table)
                os.remove("./data/change.csv")
                data[database] = db
                tab[1] = mode
                Serializable.update('./Data', 'Data', data)
                Serializable.update('./Data', 'DataTables', dataTable)
                return 0
            else:
                return 3
        else:
            return 2
    except:
        return 1        

def modoSeguro(database: str, table: str)->int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                if os.path.isfile("./Data/security/"+database+"_"+table+".json"):
                    return 4
                block.blockchain().crear(database, table)
                row = extractTable(database, table)
                if len(row):
                    for x in row:
                        block.blockchain().insert(x, database, table)
                return 0
            return 3
        return 2
    except:
        return 1

def quitarmodoSeguro(database: str, table: str)->int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                if not os.path.isfile("./Data/security/"+database+"_"+table+".json"):
                    return 4
                os.remove("./Data/security/"+database+"_"+table+".json")
                return 0
            return 3
        return 2
    except:
        return 1
#----------------Tupla-------------------#

def insert(database: str, table: str, register: list) -> int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                if tab[1] == 'avl' :
                    res = avl.insert(database, table, register)
                elif tab[1] == 'b':
                    res = b.insert(database, table, register)
                elif tab[1] == 'bplus':
                    res = bplus.insert(database, table, register)
                elif tab[1] == 'dict':
                    res = dict.insert(database, table, register)
                elif tab[1] == 'isam':
                    res = isam.insert(database, table, register)
                elif tab[1] == 'json':
                    res = json.insert(database, table, register)
                elif tab[1] == 'hash':
                    res = hash.insert(database, table, register)
                if not res:
                    if os.path.isfile("./Data/security/"+database+"_"+table+".json"):
                        block.blockchain().insert(register, database, table)
                return res
            return 3
        else:
            return 2
    except:
        return 1


def loadCSV(file: str, database: str, table: str) -> list:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                res = 3
                if tab[1] == 'avl':
                    res = avl.loadCSV(file, database, table)
                elif tab[1] == 'b':
                    res = b.loadCSV(file, database, table)
                elif tab[1] == 'bplus':
                    res = bplus.loadCSV(file, database, table)
                elif tab[1] == 'dict':
                    res = dict.loadCSV(file, database, table)
                elif tab[1] == 'isam':
                    res = isam.loadCSV(file, database, table)
                elif tab[1] == 'json':
                    res = json.loadCSV(file, database, table)
                elif tab[1] == 'hash':
                    res = hash.loadCSV(file, database, table)
                return res
            return 3
        else:
            return 2
    except:
        return 1


def extractRow(database: str, table: str, columns: list) -> list:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                if tab[1] == 'avl':
                    res = avl.extractRow(database, table, columns)
                elif tab[1] == 'b':
                    res = b.extractRow(database, table, columns)
                elif tab[1] == 'bplus':
                    res = bplus.extractRow(database, table, columns)
                elif tab[1] == 'dict':
                    res = dict.extractRow(database, table, columns)
                elif tab[1] == 'isam':
                    res = isam.extractRow(database, table, columns)
                elif tab[1] == 'json':
                    res = json.extractRow(database, table, columns)
                elif tab[1] == 'hash':
                    res = hash.extractRow(database, table, columns)
                return res
            return 3
        else:
            return 2
    except:
        return 1


def update(database: str, table: str, register: dict, columns: list) -> int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                
                if tab[1] == 'avl':
                    row = avl.extractRow(database, table, columns)
                    res = avl.update(database, table, register, columns)
                    mod = avl
                elif tab[1] == 'b':
                    row = b.extractRow(database, table, columns)
                    res = b.update(database, table, register, columns)
                    mod = b
                elif tab[1] == 'bplus':
                    row = bplus.extractRow(database, table, columns)
                    res = bplus.update(database, table, register, columns)
                    mod = bplus
                elif tab[1] == 'dict':
                    row = dict.extractRow(database, table, columns)
                    res = dict.update(database, table, register, columns)
                    mod = dict
                elif tab[1] == 'isam':
                    row = isam.extractRow(database, table, columns)
                    res = isam.update(database, table, register, columns)
                    mod = isam
                elif tab[1] == 'json':
                    row = json.extractRow(database, table, columns)
                    res = json.update(database, table, register, columns)
                    mod = json
                elif tab[1] == 'hash':
                    row = hash.extractRow(database, table, columns)
                    res = hash.update(database, table, register, columns)
                    mod = hash
                if not res:
                    if os.path.isfile('./Data/security/'+database+"_"+table+".json"):
                        row2 = row[:]
                        llave = []
                        for x in range(len(row2)):
                            if x in tab[3]:
                                llave.append(row2[x])
                        row2 = mod.extractRow(database, table, llave)
                        block.blockchain().CompararHash(row, row2, database, table)
                return res
            return 3
        else:
            return 2
    except:
        return 1


def delete(database: str, table: str, columns: list) -> int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                if tab[1] == 'avl':
                    res = avl.delete(database, table, columns)
                elif tab[1] == 'b':
                    res = b.delete(database, table, columns)
                elif tab[1] == 'bplus':
                    res = bplus.delete(database, table, columns)
                elif tab[1] == 'dict':
                    res = dict.delete(database, table, columns)
                elif tab[1] == 'isam':
                    res = isam.delete(database, table, columns)
                elif tab[1] == 'json':
                    res = json.delete(database, table, columns)
                elif tab[1] == 'hash':
                    res = hash.delete(database, table, columns)
                return res
            return 3
        else:
            return 2
    except:
        return 1


def truncate(database: str, table: str) -> int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                if tab[1] == 'avl':
                    res = avl.truncate(database, table)
                elif tab[1] == 'b':
                    res = b.truncate(database, table)
                elif tab[1] == 'bplus':
                    res = bplus.truncate(database, table)
                elif tab[1] == 'dict':
                    res = dict.truncate(database, table)
                elif tab[1] == 'isam':
                    res = isam.truncate(database, table)
                elif tab[1] == 'json':
                    res = json.truncate(database, table)
                elif tab[1] == 'hash':
                    res = hash.truncate(database, table)
                return res
            return 3
        else:
            return 2
    except:
        return 1

def cifrarDataBase(database:str):
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        dataTable = Serializable.Read('./Data/',"DataTables")
        db = data.get(database)
        if db:
            res = showTables(database)
            encrypt_row = []
            if len(res):
                for  x in res:
                    tab = dataTable.get(database+"_"+x)
                    row = extractTable(database, x)
                    for l in row:
                        # if len(tab[3]):
                        #     key = []
                        #     for t in tab[3]:
                        #         key.append(l[t])
                        #     row_encrypt = crypt.encrypt_list(l, database)
                        #     dict = {}
                        #     for g in range(len(l)):
                        #         dict.update({g:row_encrypt[g]})
                        #     print(update(database, x, dict, key))
                        # else:
                        truncate(database, x)
                        encrypt_row.append(crypt.encrypt_list(l,database))
                    import csv
                    file = open("./data/change.csv", "w", newline='', encoding='utf-8')
                    spamreader = csv.writer(file)
                    for y in encrypt_row:
                        spamreader.writerow(y)
                    file.close()
                    loadCSV("./data/change.csv", database, x)
                            
            return 0
        else:
            return 2
    except:
        return 1


def generateChecksum(database, tipo):
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            res = 1
            mode =db[1][0] 
            if mode == 'avl':
                tables = avl.showTables(database)
                mod='avl'
            elif mode == 'b':
                tables = b.showTables(database)
                mod='b'
            elif mode == 'bplus':
                tables = bplus.showTables(database)
                mod='bplus'
            elif mode == 'dict':
                tables = dict.showTables(database)
                mod='dict'
            elif mode == 'isam':
                tables = isam.showTables(database)
                mod='isam'
            elif mode == 'json':
                tables = json.showTables(database)
                mod='json'
            elif mode == 'hash':
                tables = hash.showTables(database)
                mod='hash'
            if len(tables):
                if tipo == 'MD5':
                    hash_md5 = hashlib.md5()
                elif tipo == 'SHA256':
                    hash_md5 = hashlib.sha256
                for x in tables:
                    if mod == 'avl':
                        hash_md5.update(open('./Data/avlMode/'+database+"_"+x+".tbl",'rb').read())
                    elif mod == 'b':
                        hash_md5.update(open('filename.exe','rb').read())
                    elif mod == 'isam':
                        hash_md5.update(open('filename.exe','rb').read())
                    elif mod == 'bplus':
                        hash_md5.update(open('./Data/BPlusMode/'+database+"/"+x+"/"+x+".bin",'rb').read())
                    elif mod == 'dict':
                        hash_md5.update(open('filename.exe','rb').read())
                    elif mod == 'json':
                        hash_md5.update(open('filename.exe','rb').read())
                    elif mod == 'hash':
                        hash_md5.update(open('./Data/hash/'+database+"/"+x+".bin",'rb').read())
                    return hash_md5.hexdigest()
            return res
        else:
            return 2
    except:
        return 1