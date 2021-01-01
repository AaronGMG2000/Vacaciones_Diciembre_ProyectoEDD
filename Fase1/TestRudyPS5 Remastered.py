# File:         JSON Mode Test File for EDD
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Luis Espino

import Storage as j

# assume no data exist or execute the next optional drop function
j.dropAll()

print("\nCREATE DATABASE: ")
print(j.createDatabase("DataBase1"), end="/ 0 \n")  # 0
print(j.createDatabase("DATABASE1"), end="/ 2 \n")  # 2
print(j.createDatabase("DataBase2"), end="/ 0 \n")  # 0
print(j.createDatabase("DataBase3"), end="/ 0 \n")  # 0
print(j.createDatabase("DataBase4"), end="/ 0 \n")  # 0
print(j.createDatabase("@hola"), end="/ 1 \n")  # 1
print(j.createDatabase(" "), end="/ 1 \n")  # 1
print(j.createDatabase(5), end="/ 1 \n")  # 1
print(j.createDatabase("DataBase4"), end="/ 2 \n")  # 2
print(j.showDatabases())
print("\nALTER DATABASE: ")
print(j.alterDatabase("Database1", "database2"), end="/ 3 \n")  # 3
print(j.alterDatabase("Database10", "database5"), end="/ 2 \n")  # 2
print(j.alterDatabase("Database4", "DataBase0"), end="/ 0 \n")  # 0
print(j.alterDatabase("DataBase4", "1DataBase0"), end="/ 1 \n")  # 1
print(j.showDatabases())
print("\nDROP DATABASE: ")
print(j.dropDatabase("DataBase0"), end="/ 0 \n")  # 0
print(j.dropDatabase("1DataBase0"), end="/ 2 \n")  # 2
print(j.dropDatabase("DataBase0"), end="/ 2 \n")  # 2
print(j.showDatabases())
print("\nCREATE TABLE: ")
print(j.createTable("DataBase1", "Tabla1", 5), end="/ 0 \n")  # 0
print(j.createTable("DataBase1", "Tabla2", 5), end="/ 0 \n")  # 0
print(j.createTable("DataBase1", "Tabla3", 5), end="/ 0 \n")  # 0
print(j.createTable("DataBase1", "Tabla3", 5), end="/ 3 \n")  # 3
print(j.createTable("DataBase2", "Tabla4", 4), end="/ 0 \n")  # 0
print(j.createTable("DataBase2", "Tabla5", 4), end="/ 0 \n")  # 0
print(j.createTable("DataBase2", "Tabla6", 4), end="/ 0 \n")  # 0
print(j.createTable("DataBase3", "Tabla7", 1), end="/ 0 \n")  # 0
print(j.createTable("DataBase3", "Tabla8", 3), end="/ 0 \n")  # 0
print(j.createTable("DataBase3", "Tabla9", 3), end="/ 0 \n")  # 0
print(j.createTable("DataBase3", "Tabla8", 3), end="/ 3 \n")  # 3
print(j.createTable("DataBase3", "8Tabla8", 3), end="/ 1 \n")  # 1
print(j.createTable("DataBase3", 5, 3), end="/ 1 \n")  # 1
print(j.createTable("DataBase0", "Tabla3", 3), end="/ 2 \n")  # 2
print(j.createTable("DataBase0", "1Tabla3", 3), end="/ 2 \n")  # 2
print(j.showTables("DataBase1"))
print(j.showTables("DataBase2"))
print(j.showTables("DataBase3"))
print("\nALTER ADD PK: ")
print(j.alterAddPK("DataBase1", "Tabla1", [0, 1]), end="/ 0 \n")  # 0
print(j.alterAddPK("DataBase1", "Tabla2", [1]), end="/ 0 \n")  # 0
print(j.alterAddPK("DataBase1", "Tabla3", [0]), end="/ 0 \n")  # 0
print(j.alterAddPK("DataBase2", "Tabla4", [0]), end="/ 0 \n")  # 0
print(j.alterAddPK("DataBase2", "Tabla5", [1]), end="/ 0 \n")  # 0
print(j.alterAddPK("DataBase2", "Tabla6", [1, 0]), end="/ 0 \n")  # 0
print(j.alterAddPK("DataBase1", 0, [0, 1]), end="/ 1 \n")  # 1
print(j.alterAddPK("DataBase10", "Tabla5", [0, 1]), end="/ 2 \n")  # 2
print(j.alterAddPK("DataBase1", "Tabla10", [0, 1]), end="/ 3 \n")  # 3
print(j.alterAddPK("DataBase1", "Tabla1", [0, 1]), end="/ 4 \n")  # 4
print(j.alterAddPK("DataBase3", "Tabla7", [0, 9]), end="/ 5 \n")  # 5
print("\nALTER DROP PK: ")
print(j.alterDropPK("DataBase2", "Tabla6"), end="/ 0 \n")  # 0
print(j.alterDropPK("DataBase2", 5), end="/ 1 \n")  # 1
print(j.alterDropPK("DataBase", "Tabla6"), end="/ 2 \n")  # 2
print(j.alterDropPK("DataBase2", "Tabla"), end="/ 3 \n")  # 3
print(j.alterDropPK("DataBase3", "Tabla7"), end="/ 4 \n")  # 4
print("\nALTER TABLE: ")
print(j.alterTable("DataBase1", "Tabla1", "Tabla"), end="/ 0 \n")  # 0
print(j.alterTable("DataBase1", "Tabla", "Tabla1"), end="/ 0 \n")  # 0
print(j.alterTable("DataBase1", "Tabla1", "Tabla"), end="/ 0 \n")  # 0
print(j.alterTable("DataBase1", "Tabla1", "2Tabla"), end="/ 1 \n")  # 1
print(j.alterTable("DataBase1", "Tabla1", 3), end="/ 1 \n")  # 1
print(j.alterTable("DataBase10", "Tabla1", "Tabla2"), end="/ 2 \n")  # 2
print(j.alterTable("DataBase1", "Tabla10", "Tabla2"), end="/ 3 \n")  # 3
print(j.alterTable("DataBase1", "Tabla", "Tabla2"), end="/ 4 \n")  # 4
print(j.showTables("DataBase1"))
print("\nDROP TABLE: ")
print(j.dropTable("DataBase1", "Tabla2"), end="/ 0 \n")  # 0
print(j.dropTable("DataBase1", 5), end="/ 1\n")  # 1
print(j.dropTable("DataBase", "Tabla1"), end="/ 2 \n")  # 2
print(j.dropTable("DataBase1", "Tabla1"), end="/ 3 \n")  # 3
print(j.showTables("DataBase1"))
print("\nALTER ADD COLUMN: ")
print(j.alterAddColumn("DataBase3", "Tabla7", "Hola"), end="/ 0 \n")  # 0
print(j.alterAddColumn("DataBase3", "Tabla7", 5), end="/ 0 \n")  # 0
print(j.alterAddColumn("DataBase", 58, "Hola"), end="/ 1 \n")  # 1
print(j.alterAddColumn("DataBase10", "Tabla1", "Hola"), end="/ 2 \n")  # 2
print(j.alterAddColumn("DataBase2", "Tabla", "Hola"), end="/ 3 \n")  # 3
print("\nEXTRACT TABLE []: ")
print(j.extractTable("DataBase1", "Tabla"))
print("\nINSERT: ")
print(j.insert("DataBase1", "Tabla", [1, 1, 'Guatemala', 'Guatemala', 'Guatemala']), end="/ 0 \n")  # 0
print(j.insert("DataBase1", "Tabla", [1, 2, 'Guatemala', 'Chimaltenango', 'Chimaltenango']), end="/ 0 \n")  # 0
print(j.insert("DataBase1", "Tabla", [1, 4, 'Guatemala', 'Chimaltenango', 'Chimaltenango']), end="/ 0 \n")  # 0
print(j.insert("DataBase1", "Tabla", 0), end="/ 1 \n")  # 1
print(j.insert("DataBase", "Tabla", [1, 4, 'Guatemala', 'Chimaltenango']), end="/ 2 \n")  # 2
print(j.insert("DataBase1", "Tabla10", [1, 4, 'Guatemala', 'Chimaltenango']), end="/ 3 \n")  # 3
print(j.insert("DataBase1", "Tabla", [1, 2, 'Guatemala', "Guatemala", 'Chimaltenango']), end="/ 4 \n")  # 4
print(j.insert("DataBase1", "Tabla", [1, 4, 'Guatemala', 'Chimaltenango']), end="/ 5 \n")  # 5
print("\nEXTRACT TABLE: ")
print(j.extractTable("DataBase1", "Tabla"))

print("\nCSV: ")
print(j.loadCSV("tb1.csv", "Database3", "Tabla7"))  # 0,0,0,0,0
print(j.extractTable("DataBase3", "Tabla7"))
print(j.loadCSV("tb1.csv", "Database1", "Tabla3"))  # 5,5,5,5,5
print(j.extractRow("DataBase1", "Tabla", [1, 1]))  # Correcto
print(j.extractRow("DataBase1", "Tabla", [1, 5]), end="/ [] \n")  # Incorrecto
print("\nUPDATE: ")
print(j.update("DataBase1", "Tabla", {2: "TEST", 3: "Chimaltenango", 4: "El tejar"}, [1, 1]), end="/ 0 \n")  # 0
print(j.update("DataBase1", "Tabla", {1: 10, 3: "Chimaltenango", 4: "El tejar"}, [1, 1]), end="/ 0 \n")  # 0
print(j.update("DataBase1", "Tabla", {1: 1, 3: "Chimaltenango", 4: "El tejar"}, [1, 10]), end="/ 0 \n")  # 0
print(j.update("DataBase1", "Tabla", 5, [1, 1]), end="/ 1 \n")  # 1
print(j.update("DataBase10", "Tabla", {2: "Guatemala", 3: "Chimaltenango", 4: "El tejar"}, [1, 1]), end="/ 2 \n")  # 2
print(j.update("DataBase1", "Tabla10", {2: "Guatemala", 3: "Chimaltenango", 4: "El tejar"}, [1, 1]), end="/ 3 \n")  # 3
print(j.update("DataBase1", "Tabla", {2: "Guatemala", 3: "Chimaltenango", 4: "El tejar"}, [1, 5]), end="/ 4 \n")  # 4
print(j.extractTable("DataBase1", "Tabla"))
print("\nEXTRACT ROW: ")
print(j.extractRow("DataBase1", "Tabla", [1, 1]))
print(j.extractRow("DataBase1", "Tabla", [1, 2]))
print(j.extractRow("DataBase1", "Tabla", [1, 3]), end="/ []\n")
print("\nDELETE: ")
print(j.delete("DataBase1", "Tabla", [1, 2]), end="/ 0\n")  # 0
print(j.delete("DataBase1", 0, [1, 2]), end="/ 1\n")  # 1
print(j.delete("DataBase10", "Tabla", [1, 2]), end="/ 2\n")  # 2
print(j.delete("DataBase1", "Tabla10", [1, 2]), end="/ 3\n")  # 3
print(j.delete("DataBase1", "Tabla", [1, 2]), end="/ 4\n")  # 4
print(j.extractTable("DataBase1", "Tabla"))
print("\nTRUNCATE: ")
print(j.truncate("DataBase3", "Tabla7"), end="/ 0\n")  # 0
print(j.truncate(0, "Tabla"), end="/ 1\n")  # 1
print(j.truncate("DataBase10", "Tabla"), end="/ 2\n")  # 2
print(j.truncate("DataBase1", "Tabla10"), end="/ 3\n")  # 3
print(j.extractTable("DataBase3", "Tabla7"))  # []
print("\nALTER ADD COLUMN: ")
print(j.alterAddColumn("DataBase1", "Tabla", "NUEVA"), end="/ 0\n")  # 0
print(j.extractTable("DataBase1", "Tabla"))  # Correcto
print("\nALTER DROP COLUMN: ")
print(j.alterDropColumn("DataBase1", "Tabla", 5), end="/ 0\n")  # 0
print(j.alterDropColumn("DataBase1", "Tabla", 5), end="/ 5\n")  # 5
print(j.alterDropColumn("DataBase1", "Tabla", 0), end="/ 4\n")  # 4
print(j.extractTable("DataBase1", "Tabla"))  # Correcto
print("\nALTER DROP PK: ")
print(j.alterDropPK("DataBase1", "Tabla"), end="/ 0\n")  # 0
print(j.alterDropPK("DataBase1", "Tabla"), end="/ 4\n")  # 4
print(j.extractRow("DataBase1", "Tabla", [1, 1]))
print(j.extractRow("DataBase1", "Tabla", [1]), end="/ []\n")
print(j.alterAddPK("DataBase1", "Tabla", [3]), end="/ 1\n")  # 1
print(j.alterAddPK("DataBase1", "Tabla", [0, 1]), end="/ 0\n")  # 0
print(j.alterDropColumn("DataBase1", "Tabla", 1), end="/ 4\n")  # 4
print(j.extractRow("DataBase1", "Tabla", [4]))
print("\nALTER DATABASE: ")
print(j.alterDatabase("Database1", "DataBaseTEST"), end="/ 0 \n")  # 0
print(j.extractTable("DataBaseTEST", "Tabla"))
print(j.alterDatabase("Databasetest", "DataBase1"), end="/ 0 \n")  # 0
print("\nINSERT AFTER DROP: ")
print(j.alterDropPK("DataBase1", "Tabla"), end="/ 0 \n")  # 0
print(j.insert("DataBase1", "Tabla", [1, 5, 'Guatemala', 'Peten', 'Flores']), end="/ 0 \n")  # 0
print(j.extractRow("DataBase1", "Tabla", [1]))
print(j.insert("DataBase1", "Tabla", [1, 6, 'Guatemala', 'Chimaltenango', 'Zaragoza']))
print(j.extractRow("DataBase1", "Tabla", [2]))
print(j.extractRangeTable("DataBase1", "Tabla", 1, 0, 50))
j.showCollection()
print("*******************")


print(j.showDatabases())
