from storage import storage as f
import time

f.dropAll()#limpieza de todos los datos
inicio = time.time()

#-------------------Create Database Nuevo--------------------------#
print(f.createDatabase("prueba1","bplus","ascii"),"esperado 0") 
print(f.createDatabase("prueba2","hash","utf8"),"esperado 0")
print(f.createDatabase("prueba3","b","iso-8859-1"),"esperado 0")
print(f.createDatabase("pruebá4","isam","ascii"),"esperado 0")
print(f.createDatabase("prueba5","avl","utf8"),"esperado 0")
print(f.createDatabase("prueba6","dict","iso-8859-1"),"esperado 0")
print(f.createDatabase("prueba7","json","ascii"),"esperado 0")
print(f.createDatabase("prueba7","bplus","utf8"),"esperado 2")
print(f.createDatabase("212prueba7","b","iso-8859-1"),"esperado 1")
print(f.createDatabase("212prueba7","bplus","ascii"),"esperado 1")
print(f.createDatabase("212prueba7","isam","utf8"),"esperado 1")
print(f.createDatabase("212prueba7","hash","iso-8859-1"),"esperado 1")
print(f.createDatabase("212prueba7","avl","ascii"),"esperado 1")
print(f.createDatabase("212prueba7","json","utf8"),"esperado 1")
print(f.createDatabase("212prueba7","dict","iso-8859-1"),"esperado 0")
print(f.createDatabase("212prueba7","bplus","utf"),"esperado 4")
print(f.createDatabase("212prueba7","bplu","ascii"),"esperado 3")
print(f.showDatabases())
print(f.alterDatabase('prueba1','editPrueba1'),"esperado 0")
print(f.showDatabases())
print(f.dropDatabase('editPrueba1'),"esperado 0")
print(f.showDatabases())
print(f.createDatabase("pruebaBplus","bplus","ascii"),"esperando 0")
print(f.alterDatabaseMode("prueba2","bplus"),"esperando 0")

#--------------Creación de tablas para prueba-------------------#
#Area para crear bases de datos
print("Estado BD:",f.createDatabase("BD1","hash","iso-8859-1"))#Sistema de Asignaciones
print("Estado BD:",f.createDatabase("BD2","hash","utf8"))#Sistema de Compras de productos
print("Estado BD:",f.createDatabase("BD3","hash","ascii"))#Sistema de Accesos de usuario para una base de datos
print("Estado BD:",f.createDatabase("BD4","hash","iso-8859-1"))#Sistema de Peliculas y Series para una pagina web
print("Estado BD:",f.showDatabases())#Nos deberia mostrar todas las bases de datos

#Area para crear tablas
'Creamos Tablas Estudiante, Periodo, Año, Asignacion, Curso, Asignacion_Curso'
print("---------Creamos Tabla Estudiante---------")
print("Estado Tabla:",f.createTable("BD1","Estudiante",8))
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
print("tuplas de Estudiante:", f.extractTable("BD1","Estudiante"))
# print(f.insert("BD2","Cliente",[0000000,"Helen","Valenzuela","40","facilisis@a.net",0000000,"Tokelau","Brussel"]))
#-------------------Cambiando bases de datos a otro modo-----------------#
print(f.alterDatabaseMode("BD4","hash"),'esperando 0') #Este no se que codigo pusiste pero es repetir modo de hash a hash
print(f.alterDatabaseMode("BD4","b"),'esperando 0')
print(f.alterDatabaseMode("BD4","bplus"),'esperando 0')
print(f.alterDatabaseMode("BD2","hash"),'esperando 0') #Este no se que codigo pusiste pero es repetir modo de hash a hash
print(f.alterDatabaseMode("BD3","avl"),'esperando 0')
print(f.alterDatabaseMode("BD1","dict"),'esperando 0')
print('Lista de BD1 estudiantes:',f.extractTable("BD1","Estudiante"))
print(f.alterDatabaseMode("BD2","bplus"),'esperando 0')
print(f.alterDatabaseMode("BD3","bplus"),'esperando 0')
print(f.alterDatabaseMode("BD3","avl"),'esperando 0')
print(f.alterDatabaseMode("BD3","isam"),'esperando 0')
print(f.alterTableMode("BD2","Asignacion_Curso","hash"),'esperando 3')
print(f.alterTableMode("BD2","Cliente","json"),'esperando 0')
print(f.safeModeOn("BD2","Cliente"),'esperando 0')
print(f.createDatabase("prueba11","bplus","utf8"),"esperado 0") 
print(f.createTable("prueba11","seguridad",3),'esperando 0')
print(f.alterAddPK("prueba11","seguridad",[0,1]),'esperando 0')
print(f.safeModeOn("prueba11","seguridad"),'esperando 0')
print(f.insert("prueba11","seguridad",['Prueba1','1','1']),'esperando 0')
print(f.insert("prueba11","seguridad",['1','Prueba1','1']),'esperando 0')
print(f.insert("prueba11","seguridad",['Prueba2','2','1']),'esperando 0')
print(f.insert("prueba11","seguridad",['Prueba3','3','1']),'esperando 0')
print(f.insert("prueba11","seguridad",['Prueba4','4','1']),'esperando 0')
print(f.insert("prueba11","seguridad",['Prueba5','5','1']),'esperando 0')
print(f.insert("prueba11","seguridad",['Pruebá6','1','1']),'esperando 0')
# print(f.quitarmodoSeguro("prueba11","seguridad"),'esperando 0')
print(f.update("prueba11","seguridad",{0:'Prueba'},['Pruebá6','1']),'esperando 0')
print(f.checksumDatabase("prueba11",'SHA256'))
print(f.checksumDatabase("prueba11",'MD5'))
print(f.checksumTable("prueba11","seguridad","MD5"), "checksum MD5 prueba11 seguridad")
print(f.delete("prueba11","seguridad",['Prueba2','2']),'esperando 0')
print(f.checksumDatabase("prueba11",'SHA256'), "checksum sha256 prueba11")
print(f.checksumDatabase("prueba11",'MD5'), "checksum MD5 prueba11")
print(f.checksumTable("prueba11","seguridad","MD5"), "checksum MD5 prueba11 seguridad")
print(f.checksumDatabase("BD2",'MD5'), "checksum MD5 BD2")
print(f.checksumTable("BD2","Cliente","MD5"), "checksumTable Cliente")
print(f.checksumTable("BD2","Factura","SHA256"),"cecksumTable Acceso")
print(f.delete("BD2","Factura",[85274644]), 'esperando 0')
print(f.checksumDatabase("BD2",'MD5'), "checksum2 MD5 BD2")
print(f.delete("BD2","Producto",[42527769]), 'esperando 0')
print(f.checksumDatabase("BD2",'MD5'), "checksum3 MD5 BD2")
print("Estado PKS:",f.alterAddPK("BD2","Orden",[0]), 'esperando 0')
print(f.checksumDatabase("BD2",'MD5'), "checksum4 MD5 BD2")
print(f.checksumTable("BD2","Cliente","MD5"), "checksumTable2 Cliente")
print(f.checksumTable("BD2","Factura","SHA256"),"cecksumTable2 Acceso")
print(f.encrypt("BD2","Contraseña"),'esperando gAAAAABf9O34zwfU3QM0YKTUFrt9I08-mqm43SB2z5Q81yyGuaMEWtNx6JVEnjq6f8h28j4uA9Z4hCRk9-Io80qYQNFKwaciBA==')
print(f.decrypt("gAAAAABf9O34zwfU3QM0YKTUFrt9I08-mqm43SB2z5Q81yyGuaMEWtNx6JVEnjq6f8h28j4uA9Z4hCRk9-Io80qYQNFKwaciBA==","Contraseña"),'esperando BD2')
print(f.alterDatabaseEncoding("prueba11","iso-8859-1"))
print(f.extractTable("prueba11","seguridad"))
print(f.alterDatabaseEncoding("prueba11","utf8"))

# print(f.extractTable("BD2","Cliente"))
final = time.time()
print("------------------------------------------------------------------")
print("Tiempo de Ejecucion:", final-inicio, "segundos")
print(f.extractTable("BD1","Periodo"))
print(f"Compresion {f.alterTableCompress('BD1','Periodo',7)}")
print(f.extractTable("BD1","Periodo"))
print(f"Decompresion {f.alterTableDecompress('BD1','Periodo')}")
print(f.extractTable("BD1","Periodo"))