from storage import storage as f
import time

f.dropAll()
inicio = time.time()
#-------------------Create Database Nuevo--------------------------#
print("CREATE DATABASE: (avl): ",f.createDatabase("DBavl","avl","utf8"),"/ 0")
print("CREATE DATABASE: (b): ",f.createDatabase("DBb","b","utf8"),"/ 0")
print("CREATE DATABASE: (bplus): ",f.createDatabase("DBbplus","bplus","utf8"),"/ 0")
print("CREATE DATABASE: (dict)",f.createDatabase("DBdict","dict","utf8"),"/ 0")
print("CREATE DATABASE: (hash)",f.createDatabase("DBhash","hash","utf8"),"/ 0")
print("CREATE DATABASE: (isam)",f.createDatabase("DBisam","isam","utf8"),"/ 0")
print("CREATE DATABASE: (json)",f.createDatabase("DBjson","json","utf8"),"/ 0")
print("CREATE DATABASE: (áéíóú)",f.createDatabase("áéíóú","json","utf8"),"/ 0")
print("CREATE DATABASE: ",f.createDatabase("85DBav","avl","utf8"),"/1")
print("CREATE DATABASE: ",f.createDatabase(2,"avl","utf8"),"/1")
print("CREATE DATABASE: ",f.createDatabase("DBavl","avl","utf8"),"/ 2")
print("CREATE DATABASE: ",f.createDatabase("DBhashplus","hashplus","utf8"),"/ 3")
print("CREATE DATABASE: ",f.createDatabase("DBhashplus","hashplus","utf8"),"/ ¿3-2?")
print("CREATE DATABASE: ",f.createDatabase("DBhashplus","hashplus","utf8plis"),"/ ¿4-3-2?")
print("CREATE DATABASE: ",f.createDatabase("DBavl2","avl","utf8plus"),"/ 4\n")

print("SHOW DATABASE: ",f.showDatabases(),"\n")

print("ALTER DATABASE: ",f.alterDatabase('áéíóú','editPrueba1'),"/ 0")
print("ALTER DATABASE: ",f.alterDatabase(5,'editPrueba1'),"/ 1")
print("ALTER DATABASE: ",f.alterDatabase("test",'editPrueba1'),"/ 2")
print("ALTER DATABASE: ",f.alterDatabase('editPrueba1','editPrueba1'),"/ 3\n")

print("SHOW DATABASE: ", f.showDatabases(), "\n")

print("DROP DATABASE: ",f.dropDatabase('editPrueba1'),"/ 0")
print("SHOW DATABASE: ",f.showDatabases())
print("ALTER DATABASE MODE: ",f.alterDatabaseMode("DBavl","b"),"/ 0")

print("********** DROP ALL: ",f.dropAll())

#--------------Creación de tablas para prueba-------------------#
#Area para crear bases de datos
print("CREATE DATABASE: ",f.createDatabase("BD1","hash","utf8"),"/ 0")#Sistema de Asignaciones
print("CREATE DATABASE: ",f.createDatabase("BD2","hash","utf8"),"/ 0")#Sistema de Compras de productos
print("CREATE DATABASE: ",f.createDatabase("BD3","hash","utf8"),"/ 0")#Sistema de Accesos de usuario para una base de datos
print("CREATE DATABASE: ",f.createDatabase("BD4","hash","utf8"),"/ 0\n")#Sistema de Peliculas y Series para una pagina web

print("SHOW DATABASE: ",f.showDatabases(),"\n")
print("ALTER DATABASE MODE (TO avl): ",f.alterDatabaseMode("BD1","avl"),"/ 0")
print("ALTER DATABASE MODE (TO b): ",f.alterDatabaseMode("BD1","b"),"/ 0")
print("ALTER DATABASE MODE (TO bplus): ",f.alterDatabaseMode("BD1","bplus"),"/ 0")
print("ALTER DATABASE MODE (TO dict): ",f.alterDatabaseMode("BD1","dict"),"/ 0")
print("ALTER DATABASE MODE (TO isam): ",f.alterDatabaseMode("BD1","isam"),"/ 0")
print("ALTER DATABASE MODE (TO json): ",f.alterDatabaseMode("BD1","json"),"/ 0")
print("ALTER DATABASE MODE (TO hash): ",f.alterDatabaseMode("BD1","hash"),"/ 0")
print("ALTER DATABASE MODE (TO avl): ",f.alterDatabaseMode("BD1","avl"),"/ 0\n")

#Area para crear tablas
'Creamos Tablas Estudiante, Periodo, Año, Asignacion, Curso, Asignacion_Curso'
print("---------Creamos Tabla Estudiante---------")
print("CREATE TABLE:",f.createTable("BD1","Estudiante",8))
print("Estado PKS:",f.alterAddPK("BD1","Estudiante",[0]))
print("Estado Inserts",f.loadCSV("./BD1/Estudiantes.csv","BD1","Estudiante"))

print("---------Creamos Tabla Periodo---------")
print("Estado Tabla:",f.createTable("BD1","Periodo",2))
print("Estado PKS:",f.alterAddPK("BD1","Periodo",[0]))
print("Estado Inserts",f.loadCSV("./BD1/Periodo.csv","BD1","Periodo"))

print("---------Creamos Tabla Año---------")
print("Estado Tabla:",f.createTable("BD1","Year",2))
print("Estado PKS:",f.alterAddPK("BD1","Year",[0]))
print("Estado Inserts",f.loadCSV("./BD1/Año.csv","BD1","Year"))
print("[BD1] Year\n:", f.extractTable("BD1","Year"))

print("---------Creamos Tabla Curso---------")
print("Estado Tabla:",f.createTable("BD1","Curso",2))
print("Estado PKS:",f.alterAddPK("BD1","Curso",[0]))
print("Estado Inserts",f.loadCSV("./BD1/Curso.csv","BD1","Curso"))

print("---------Creamos Tabla Asignacion---------")
print("Estado Tabla:",f.createTable("BD1","Asignacion",4))
print("Estado PKS:",f.alterAddPK("BD1","Asignacion",[0]))
print("Estado Inserts",f.loadCSV("./BD1/Asignacion.csv","BD1","Asignacion"))

print("---------Creamos Tabla Asignacion_Curso---------")
print("Estado Tabla:",f.createTable("BD1","Asignacion_Curso",2))
print("Estado Inserts",f.loadCSV("./BD1/Asignacion_Curso.csv","BD1","Asignacion_Curso"))


'Creamos Tablas para Compras, Tablas: Cliente, Factura, Producto, Orden'
print("---------Creamos Tabla Cliente---------")
print("Estado Tabla:",f.createTable("BD2","Cliente",8))
print("Estado PKS:",f.alterAddPK("BD2","Cliente",[0]))
print("Estado Inserts",f.loadCSV("./BD2/Cliente.csv","BD2","Cliente"))

print("---------Creamos Tabla Producto---------")
print("Estado Tabla:",f.createTable("BD2","Producto",3))
print("Estado PKS:",f.alterAddPK("BD2","Producto",[0]))
print("Estado Inserts",f.loadCSV("./BD2/Producto.csv","BD2","Producto"))

print("---------Creamos Tabla Factura---------")
print("Estado Tabla:",f.createTable("BD2","Factura",4))
print("Estado PKS:",f.alterAddPK("BD2","Factura",[0]))
print("Estado Inserts",f.loadCSV("./BD2/Factura.csv","BD2","Factura"))

print("---------Creamos Tabla Orden---------")
print("Estado Tabla:",f.createTable("BD2","Orden",3))
print("Estado Inserts",f.loadCSV("./BD2/Orden.csv","BD2","Orden"))

'Creamos tablas para base de datos 2'
print("---------Creamos Tabla Usuario---------")
print("Estado Tabla:",f.createTable("BD3","Usuario",8))
print("Estado PKS:",f.alterAddPK("BD3","Usuario",[0]))
print("Estado Inserts",f.loadCSV("./BD3/Personas.csv","BD3","Usuario"))

print("---------Creamos Tabla Privilegio---------")
print("Estado Tabla:",f.createTable("BD3","Privilegio",3))
print("Estado PKS:",f.alterAddPK("BD3","Privilegio",[0]))
print("Estado Inserts",f.loadCSV("./BD3/Privilegios.csv","BD3","Privilegio"))

print("---------Creamos Tabla Acceso---------")
print("Estado Tabla:",f.createTable("BD3","Acceso",2))
print("Estado PKS:", f.alterAddPK("BD3","Acceso",[0,1]))
print("Estado Inserts",f.loadCSV("./BD3/Acceso.csv","BD3","Acceso"))

'Creamos tablas para sistema de peliculas y series'
print("---------Creamos Tabla Pelicula---------")
print("Estado Tabla:",f.createTable("BD4","Pelicula",5))
print("Estado Inserts",f.loadCSV("./BD4/Pelicula.csv","BD4","Pelicula"))

print("---------Creamos Tabla Serie---------")
print("Estado Tabla:",f.createTable("BD4","Serie",5))
print("Estado PKS:", f.alterAddPK("BD4","Serie",[0]))
print("Estado Inserts",f.loadCSV("./BD4/Serie.csv","BD4","Serie"))

print("---------Creamos Tabla Capitulo---------")
print("Estado Tabla:",f.createTable("BD4","Capitulo",5))
print("Estado Inserts",f.loadCSV("./BD4/Capitulo.csv","BD4","Capitulo"))

print("------------------Listado de Tablas de las bases de datos-----------------------")
print("Tablas de BD1:",f.showTables("BD1"))
print("Tablas de BD2:",f.showTables("BD2"))
print("Tablas de BD3:",f.showTables("BD3"))
print("Tablas de BD4:",f.showTables("BD4"))



print("ALTER DATABASE MODE (TO bplus): ",f.alterDatabaseMode("BD1","bplus"),"/ 0\n")
# print("[BD1] Estudiante:", f.extractTable("BD1","Estudiante"))
# print(f.insert("BD2","Cliente",[0000000,"Helen","Valenzuela","40","facilisis@a.net",0000000,"Tokelau","Brussel"]))
#-------------------Cambiando bases de datos a otro modo-----------------#
print("ALTER DATABASE MODE (TO hash): ",f.alterDatabaseMode("BD4","hash"),'/ 1') #Este no se que codigo pusiste pero es repetir modo de hash a hash
print("ALTER DATABASE MODE (TO b): ",f.alterDatabaseMode("BD4","b"),'/ 0')
print("ALTER DATABASE MODE (TO bplus): ",f.alterDatabaseMode("BD4","bplus"),'/ 0\n')

print("ALTER DATABASE MODE (TO hash): ",f.alterDatabaseMode("BD2","hash"),'/ 1') #Este no se que codigo pusiste pero es repetir modo de hash a hash
print("ALTER DATABASE MODE (TO avl): ",f.alterDatabaseMode("BD3","avl"),'/ 0')
print("ALTER DATABASE MODE (TO dict): ",f.alterDatabaseMode("BD1","dict"),'/ 0')
# print('Lista de BD1 estudiantes:',f.extractTable("BD1","Estudiante"))
print("ALTER DATABASE MODE (TO bplus): ",f.alterDatabaseMode("BD2","bplus"),'/ 0')
print("ALTER DATABASE MODE (TO bplus): ",f.alterDatabaseMode("BD3","bplus"),'/ 0')
print("ALTER DATABASE MODE (TO avl): ",f.alterDatabaseMode("BD3","avl"),'/ 0')
print("ALTER DATABASE MODE (TO isam): ",f.alterDatabaseMode("BD3","isam"),'/ 0')
print("ALTER DATABASE MODE (TO ???): ",f.alterDatabaseMode("BD3","wtf"),'/ 4\n')

print("ALTER TABLE MODE (TO hash): ",f.alterTableMode("BD2","Asignacion_Curso","hash"),'/ 3')
print("ALTER TABLE MODE (TO json): ",f.alterTableMode("BD2","Cliente","json"),'/ 0\n')

print("SAFEMODE ON: ",f.safeModeOn("BD2","Cliente"),'/ 0')
print("CREATE DATABASE: (avl): ",f.createDatabase("TEST","avl","utf8"),"/ 0") 
print("CREATE TABLE: ",f.createTable("TEST","seguridad",3),'/ 0')
print("TABLE ADD PK: ", f.alterAddPK("TEST","seguridad",[0,1]),'/ 0')
print("SAFEMODE ON: ",f.safeModeOn("TEST","seguridad"),'/ 0')
print("INSERT INTO TABLE: ",f.insert("TEST","seguridad",['Prueba1','1',True]),'/ 0')
print("INSERT INTO TABLE: ",f.insert("TEST","seguridad",['1','Prueba1',True]),'/ 0')
print("INSERT INTO TABLE: ",f.insert("TEST","seguridad",['Prueba2','2',False]),'/ 0')
print("INSERT INTO TABLE: ",f.insert("TEST","seguridad",['Prueba3','3',False]),'/ 0')
print("INSERT INTO TABLE: ",f.insert("TEST","seguridad",['Prueba4','4',False]),'/ 0')
print("INSERT INTO TABLE: ",f.insert("TEST","seguridad",['Prueba5','5',False]),'/ 0')
print("INSERT INTO TABLE: ",f.insert("TEST","seguridad",['Pruebá6','1',False]),'/ 0\n')

print("ALTER TABLE MODE (TO json): ",f.alterTableMode("TEST","seguridad","json"),'/ 0')
print("ALTER TABLE MODE (TO avl): ",f.alterTableMode("TEST","seguridad","avl"),'/ 0')
print("UPDATE TABLE: ",f.update("TEST","seguridad",{0:'Prueba'},['Pruebá6','1']),'/ 0\n')

print("CHECKSUM DATABASE (SHA256): ",f.checksumDatabase("TEST",'SHA256'))
print("CHECKSUM DATABASE (MD5): ",f.checksumDatabase("TEST",'MD5'))
print("CHECKSUM DATABASE (MGR): ",f.checksumDatabase("TEST",'MGR'),'/ None\n')

print("CHECKSUM TABLE (SHA256): ",f.checksumTable("TEST","seguridad","SHA256"))
print("CHECKSUM TABLE (SHA256 AGAIN): ",f.checksumTable("TEST","seguridad","SHA256"))
print("CHECKSUM TABLE (MD5): ",f.checksumTable("TEST","seguridad","MD5"))
print("CHECKSUM TABLE (MD5 AGAIN): ",f.checksumTable("TEST","seguridad","MD5"))
print("CHECKSUM TABLE (MGR): ",f.checksumTable("TEST","seguridad","MGR"),"\n")

print("BEFORE DELETE ---")
print("DELETE TUPLE: ", f.delete("TEST","seguridad",['Prueba2','2']),'/ 0')
print("CHECKSUM DATABASE (SHA256): ",f.checksumDatabase("TEST",'SHA256'))
print("CHECKSUM DATABASE (MD5): ",f.checksumDatabase("TEST",'MD5'))
print("CHECKSUM TABLE (SHA256): ",f.checksumTable("TEST","seguridad","SHA256"))
print("CHECKSUM TABLE (MD5): ",f.checksumTable("TEST","seguridad","MD5"),"\n")

print("OTHER DATABASE ND TABLES  ---")
print("CHECKSUM DATABASE (MD5): ", f.checksumDatabase("BD2",'MD5'))
print("CHECKSUM TABLE (SHA256): ",f.checksumTable("BD2","Cliente","SHA256"))
print("CHECKSUM TABLE (SHA256): ",f.checksumTable("BD2","Factura","SHA256"),"\n")

print("BEFORE DELETE ---")
print("DELETE TUPLE: ", f.delete("BD2","Factura",[85274644]), '/ 0')
print("DELETE TUPLE: ", f.delete("BD2","Producto",[42527769]), '/ 0')
print("CHECKSUM DATABASE (MD5): ", f.checksumDatabase("BD2",'MD5'))
print("CHECKSUM TABLE (SHA256): ",f.checksumTable("BD2","Cliente","SHA256"))
print("CHECKSUM TABLE (SHA256): ",f.checksumTable("BD2","Factura","SHA256"),"\n")

print("BEFORE ALTER AD PK ---")
print("CHECKSUM DATABASE (MD5): ", f.checksumDatabase("BD2",'MD5'))
print("ALTER ADD PK: ",f.alterAddPK("BD2","Orden",[0]), '/ 0')
print("CHECKSUM DATABASE (MD5): ", f.checksumDatabase("BD2",'MD5'))
print("CHECKSUM TABLE (SHA256): ",f.checksumTable("BD2","Cliente","SHA256"))
print("CHECKSUM TABLE (SHA256): ",f.checksumTable("BD2","Factura","SHA256"),"\n")

var = f.encrypt("PATO","SANDÍA")
print("ENCRYPT (PATO, SANDÍA): ",var)
print("ENCRYPT (PATO, SANDÍA): ",var)
print("DECRYPT: ", f.decrypt(var,"SANDÍA"),'/ PATO\n')

print("ALTER DATABASE ENCODING: ", f.alterDatabaseEncoding("TEST","iso-8859-1"), "/ 0")
print("ALTER DATABASE ENCODING: ", f.alterDatabaseEncoding("TEST","iso-8859-10"), "/ 3")
print("ALTER DATABASE ENCODING: ",f.alterDatabaseEncoding("TEST","utf8"))
print(f.extractTable("BD1","Periodo"),"/ 0\n")

print('******************************************************************************')
print(f.extractTable("BD1","Periodo"))
print("DATABASE COMPRESS: ",f.alterDatabaseCompress('BD1',2),"/ 0")
print("TABLE COMPRESS: ",f.alterTableCompress('BD1','Periodo',2),"/ 1")
print(f.extractTable("BD1","Periodo"))
print("TABLE DECOMPRESS: ",f.alterTableDecompress('BD1','Periodo'),"/ 0")
print("DATABASE DECOMPRESS: ",f.alterDatabaseDecompress('BD1'),"/ 0")
print("TABLE DECOMPRESS: ",f.alterTableDecompress('BD1','Periodo'),"/ 3")
print(f.extractTable("BD1","Periodo"), "\n")

print("TABLE COMPRESS: ",f.alterTableCompress('BD1','Periodo',2),"/ 0")
print("INSERT : ", f.insert('BD1','Periodo', [10,'Primer Semestre']), "/ 0")
print("UPDATE : ", f.update('BD1','Periodo', {1:'CAMBIO'}, [2]), "/ 0")
print("EXTRACT ROW", f.extractRow("BD1","Periodo", [2]),"\n")
print("ALTER ADD COLUMN : ", f.alterAddColumn("BD1","Periodo", "TEST"),"\n")
print(f.extractTable("BD1","Periodo"))
print("TABLE DECOMPRESS: ",f.alterTableDecompress('BD1','Periodo'),"/ 0")
print(f.extractTable("BD1","Periodo"),"\n")
print("EXTRACT ROW", f.extractRow("BD1","Periodo", [2]),"\n")
print("", f.alterTableAddFK("BD1","Periodo", "index", [0], "Year", [0]), "/ 0")
print("", f.alterTableAddFK("BD1","Year", "index", [0], "Periodo", [0]), "/ 1")
print("", f.alterTableAddFK("BD1","Year", "index2", [0], "Periodo", [0]), "/ 1")
print("", f.alterTableDropFK("BD1","Periodo", "index"), "/ 0\n")

print("\n ---UNIQUE-----")
print("CREATE DATABASE: (avl): ",f.createDatabase("CALIFICACION","avl","utf8"),"/ 0")
print("CREAR TABLA:", f.createTable("CALIFICACION","UNIQUE",2), "/ ", 0)
print("ADD UNIQUE:", f.alterTableAddUnique("NOEXISTE","UNIQUE","id_unico",[0]), "/ ",2)
print("ADD UNIQUE:", f.alterTableAddUnique("CALIFICACION","NOEXISTE","id_unico",[0]), "/ ",3)
print("ADD UNIQUE:", f.alterTableAddUnique("CALIFICACION","UNIQUE","id_unico",[5]), "/ ",4)
print("ADD UNIQUE:", f.alterTableAddUnique("CALIFICACION","UNIQUE","id_unico",[0]), "/ ",0)
print("INSERT TABLA:",f.insert("CALIFICACION","UNIQUE",["t1","Carlos"]), "/ ",0)
print("INSERT TABLA:",f.insert("CALIFICACION","UNIQUE",["t1","Andree"]), "/ ¿4,0?",)
print("DROP UNIQUE:", f.alterTableDropUnique("NOEXISTE","UNIQUE","id_unico"),"/ ",2)
print("DROP UNIQUE:", f.alterTableDropUnique("CALIFICACION","NOEXISTE","id_unico"),"/ ",3)
print("DROP UNIQUE:", f.alterTableDropUnique("CALIFICACION","UNIQUE","id_noexiste"),"/ ",4,"\n")
# print("DROP UNIQUE:", f.alterTableDropUnique("CALIFICACION","UNIQUE","id_unico"),"/ ",0)
print("\n ---INDEX-----")
print("CREAR TABLA:", f.createTable("CALIFICACION","INDEX",2), "/ ", 0)
print("ADD INDEX: ", f.alterTableAddIndex("NOEXISTE","INDEX","id_unico",[0]), "/ ",2)
print("ADD INDEX: ", f.alterTableAddIndex("CALIFICACION","NOEXISTE","id_unico",[0]), "/ ",3)
print("ADD INDEX: ", f.alterTableAddIndex("CALIFICACION","INDEX","id_unico",[5]), "/ ",4)
print("ADD INDEX: ", f.alterTableAddIndex("CALIFICACION","INDEX","id_unico",[0]), "/ ",0)
print("INSERT TABLA:",f.insert("CALIFICACION","INDEX",["t1","Carlos"]), "/ ",0)
print("INSERT TABLA:",f.insert("CALIFICACION","INDEX",["t1","Andree"]), "/ ¿4,0?",)
print("DROP INDEX: ", f.alterTableDropIndex("NOEXISTE","INDEX","id_unico"),"/ ",2)
print("DROP INDEX: ", f.alterTableDropIndex("CALIFICACION","NOEXISTE","id_unico"),"/ ",3)
print("DROP INDEX: ", f.alterTableDropIndex("CALIFICACION","INDEX","id_noexiste"),"/ ",4)
# print("DROP INDEX :", f.alterTableDropIndex("CALIFICACION","INDEX","id_unico"),"/ ",0)
final = time.time()
print("------------------------------------------------------------------")
print("Tiempo de Ejecucion:", final-inicio, "segundos")
