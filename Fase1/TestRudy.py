# File:         JSON Mode Test File for EDD
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Luis Espino

import Storage  as j
from time import time
import random
# assume no data exist or execute the next optional drop function
j.dropAll()

# print(j.createDatabase("DataBase2")) #0
# print(j.createDatabase("DataBase3")) #0
# print(j.createDatabase("DataBase4")) #0
# print(j.createDatabase("@hola")) #1
# print(j.createDatabase("DataBase4")) #2
# print(j.showDatabases())
# print(j.alterDatabase("Database1","database2")) #3
# print(j.alterDatabase("Database","database2")) #2
# print(j.alterDatabase("Database4","DataBase0")) #0
# print(j.alterDatabase("DataBase4","1DataBase0")) #1
# print(j.showDatabases())
# print(j.dropDatabase("DataBase0")) #0
# print(j.dropDatabase("1DataBase0")) #1
# print(j.dropDatabase("DataBase0")) #2
# print(j.showDatabases())
# print(j.createTable("DataBase1","Tabla1",5)) #0
# print(j.createTable("DataBase1","Tabla2",5)) #0
# print(j.createTable("DataBase1","Tabla3",5)) #0
# print(j.createTable("DataBase2","Tabla4",4)) #0
# print(j.createTable("DataBase2","Tabla5",4)) #0
# print(j.createTable("DataBase2","Tabla6",4)) #0
# print(j.createTable("DataBase3","Tabla7",3)) #0
# print(j.createTable("DataBase3","Tabla8",3)) #0
# print(j.createTable("DataBase3","Tabla9",3)) #0
# print(j.createTable("DataBase3","Tabla8",3)) #3
# print(j.createTable("DataBase0","Tabla3",3)) #2
# print(j.createTable("DataBase0","1Tabla3",3)) #1
# print(j.showTables("DataBase1"))
# print(j.showTables("DataBase2"))
# print(j.showTables("DataBase3"))
# print(j.alterAddPK("DataBase1","Tabla1",[0,1])) #0
# print(j.alterAddPK("DataBase1","Tabla2",[1])) #0
# print(j.alterAddPK("DataBase1","Tabla3",[0])) #0
# print(j.alterAddPK("DataBase2","Tabla4",[0])) #0
# print(j.alterAddPK("DataBase2","Tabla5",[1])) #0
# print(j.alterAddPK("DataBase2","Tabla6",[1,0])) #0
# print(j.alterAddPK("DataBase1","Tabla1",[0,1])) #4
# print(j.alterAddPK("DataBase1","Tabla1",[0,5])) #5
# print(j.alterAddPK("DataBase0","Tabla1",[0,5])) #2
# print(j.alterAddPK("DataBase1","Tabla",[0,5])) #3
# print(j.alterDropPK("DataBase2","Tabla6")) #0
# print(j.alterDropPK("DataBase2","Tabla")) #3
# print(j.alterDropPK("DataBase","Tabla6")) #2
# print(j.alterTable("DataBase1","Tabla1","Tabla")) #0
# print(j.alterTable("DataBase1","Tabla","Tabla2")) #4
# print(j.alterTable("DataBase1","Tabla1","Tabla")) #3
# print(j.alterTable("DataBase","Tabla","Tabla1")) #2
# print(j.showTables("DataBase1"))
# print(j.dropTable("DataBase1","Tabla2")) #0
# print(j.dropTable("DataBase1","Tabla1")) #2
# print(j.dropTable("DataBase","Tabla1")) #3
# print(j.showTables("DataBase1"))
# print(j.alterAddColumn("DataBase2","Tabla","Hola")) #3
# print(j.alterAddColumn("DataBase","Tabla","Hola")) #2
# print(j.alterAddColumn("DataBase1","Tabla1","Hola")) #3
# print(j.extractTable("DataBase1","Tabla"))
# print(j.insert("DataBase1","Tabla",[1,1,'Guatemala','Guatemala','Guatemala'])) #0
# print(j.insert("DataBase1","Tabla",[1,2,'Guatemala','Chimaltenango','Chimaltenango'])) #0
# print(j.insert("DataBase1","Tabla",[1,3,'Guatemala','Chimaltenango','San Martin Jilotepeque'])) #0
# print(j.insert("DataBase1","Tabla",[1,3,'Guatemala','Chimaltenango','San Martin Jilotepeque'])) #4
# print(j.insert("DataBase1","Tabla",[1,4,'Guatemala','Chimaltenango'])) #5
# print(j.insert("DataBase","Tabla",[1,4,'Guatemala','Chimaltenango'])) #2
# print(j.insert("DataBase1","Tabla1",[1,4,'Guatemala','Chimaltenango'])) #3
# print(j.extractTable("DataBase1","Tabla"))
# print(j.loadCSV("./tb1.csv","Database3","Tabla7")) # 0,0,0,0,0
# print(j.extractTable("DataBase3","Tabla7"))
# print(j.loadCSV("./tb1.csv","Database1","Tabla3")) # 5,5,5,5,5
# print(j.extractRow("DataBase1","Tabla",[1,1])) # Correcto
# print(j.extractRow("DataBase1","Tabla",[1,5])) # Incorrecto
# print(j.update("DataBase1","Tabla",{2:"Guatemala",3: "Chimaltenango", 4: "El tejar"}, [1,1])) #0
# print(j.update("DataBase1","Tabla",{2:"Guatemala",3: "Chimaltenango", 4: "El tejar"}, [1,4])) #4
# print(j.update("DataBase1","Tabla",{1:2,2:"Guatemala",3: "Chimaltenango", 4: "El tejar"}, [1,1])) #1
# print(j.extractRow("DataBase1","Tabla",[1,1])) # Correcto
# print(j.delete("DataBase1","Tabla",[1,1])) # 0
# print(j.delete("DataBase1","Tabla",[1,1])) # 4
# print(j.extractTable("DataBase1","Tabla")) # Correcto
# print(j.truncate("DataBase3","Tabla7")) #0
# print(j.extractTable("DataBase3","Tabla7")) # []
# print(j.alterAddColumn("DataBase1","Tabla","None")) #0
# print(j.extractTable("DataBase1","Tabla")) # Correcto
# print(j.alterDropColumn("DataBase1","Tabla",5)) #0
# print(j.alterDropColumn("DataBase1","Tabla",5)) #5
# print(j.alterDropColumn("DataBase1","Tabla",0)) #4
# print(j.extractTable("DataBase1","Tabla")) # Correcto
# print(j.alterDropPK("DataBase1","Tabla")) #0
# print(j.alterDropPK("DataBase1","Tabla")) #4
# print(j.extractRow("DataBase1","Tabla",[1,2])) #Correcto
# print(j.alterAddPK("DataBase1", "Tabla",[2])) #1
# print(j.alterAddPK("DataBase1", "Tabla",[1])) #0
# print(j.extractRow("DataBase1","Tabla",[2])) #Correcto
# #Aqui vamos a forzar una reorganización de datos al ingresar 2 datos nuevos
# #Esto debido a que el incrementable hara conflicto
# print(j.alterDropPK("DataBase1","Tabla")) #0
# print(j.insert("DataBase1","Tabla",[1,5,'Guatemala','Peten','Flores'])) #0
# print(j.extractRow("DataBase1","Tabla",[3])) #Correcto
# print(j.insert("DataBase1","Tabla",[1,6,'Guatemala','Chimaltenango','Zaragoza'])) #0 En este punto reorganizara
# #Podemos ver que se reorganizo el arbol debido a que el dato 1,6 deberia corresponder 
# #a la PK 2 oculta
# print(j.extractRow("DataBase1","Tabla",[2])) #Incorrecto, Se puede ver que se reorganizo
# print("*******************")
# print(j.extractRangeTable("DataBase1","Tabla",1, 2,3)) #imprime pk 2 y 3
start_time = time()
print(j.createDatabase("DataBase2")) #0

print(j.createTable("DataBase2","TablaMuerte",4))
print(j.loadCSV("./tb1.csv","DataBase2","TablaMuerte"))
elapsed_time = time() - start_time
print(j.extractTable("DataBAse2","TablaMuerte"))
list = []
for x in range(1,245):
    list.append(x)
while len(list)>3:
    x = random.randint(0,len(list)-1)
    y = list.pop(x)
    print(j.delete("DataBase2","TablaMuerte",[y]))
print("Elapsed time: %.10f seconds." % elapsed_time)
