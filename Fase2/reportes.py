from storage import storage2 as j
import time

j.dropAll()#limpieza de todos los datos
inicio = time.time()

#Area para crear bases de datos
print("Estado BD:",j.createDatabase("BD1","json","utf8"))#Sistema de Asignaciones
print("Estado BD:",j.createDatabase("BD2","json","utf8"))#Sistema de Compras de productos
print("Estado BD:",j.createDatabase("BD3","json","utf8"))#Sistema de Accesos de usuario para una base de datos
print("Estado BD:",j.createDatabase("BD4","json","utf8"))#Sistema de Peliculas y Series para una pagina web
print("Estado BD:",j.showDatabases())#Nos deberia mostrar todas las bases de datos

#Area para crear tablas
'Creamos Tablas Estudiante, Periodo, Año, Asignacion, Curso, Asignacion_Curso'
print("---------Creamos Tabla Estudiante---------")
print("Estado Tabla:",j.createTable("BD1","Estudiante",8))
print("Estado PKS:",j.alterAddPK("BD1","Estudiante",[0]))
print("Estado Inserts",j.loadCSV("./BD1/Estudiantes.csv","BD1","Estudiante"))

print("---------Creamos Tabla Periodo---------")
print("Estado Tabla:",j.createTable("BD1","Periodo",2))
print("Estado PKS:",j.alterAddPK("BD1","Periodo",[0]))
print("Estado Inserts",j.loadCSV("./BD1/Periodo.csv","BD1","Periodo"))

print("---------Creamos Tabla Año---------")
print("Estado Tabla:",j.createTable("BD1","Year",2))
print("Estado PKS:",j.alterAddPK("BD1","Year",[0]))
print("Estado Inserts",j.loadCSV("./BD1/Año.csv","BD1","Year"))

print("---------Creamos Tabla Curso---------")
print("Estado Tabla:",j.createTable("BD1","Curso",2))
print("Estado PKS:",j.alterAddPK("BD1","Curso",[0]))
print("Estado Inserts",j.loadCSV("./BD1/Curso.csv","BD1","Curso"))

print("---------Creamos Tabla Asignacion---------")
print("Estado Tabla:",j.createTable("BD1","Asignacion",4))
print("Estado PKS:",j.alterAddPK("BD1","Asignacion",[0]))
print("Estado Inserts",j.loadCSV("./BD1/Asignacion.csv","BD1","Asignacion"))

print("---------Creamos Tabla Asignacion_Curso---------")
print("Estado Tabla:",j.createTable("BD1","Asignacion_Curso",2))
print("Estado Inserts",j.loadCSV("./BD1/Asignacion_Curso.csv","BD1","Asignacion_Curso"))


'Creamos Tablas para Compras, Tablas: Cliente, Factura, Producto, Orden'
print("---------Creamos Tabla Cliente---------")
print("Estado Tabla:",j.createTable("BD2","Cliente",8))
print("Estado PKS:",j.alterAddPK("BD2","Cliente",[0]))
print("Estado Inserts",j.loadCSV("./BD2/Cliente.csv","BD2","Cliente"))

print("---------Creamos Tabla Producto---------")
print("Estado Tabla:",j.createTable("BD2","Producto",3))
print("Estado PKS:",j.alterAddPK("BD2","Producto",[0]))
print("Estado Inserts",j.loadCSV("./BD2/Producto.csv","BD2","Producto"))

print("---------Creamos Tabla Factura---------")
print("Estado Tabla:",j.createTable("BD2","Factura",4))
print("Estado PKS:",j.alterAddPK("BD2","Factura",[0]))
print("Estado Inserts",j.loadCSV("./BD2/Factura.csv","BD2","Factura"))

print("---------Creamos Tabla Orden---------")
print("Estado Tabla:",j.createTable("BD2","Orden",3))
print("Estado Inserts",j.loadCSV("./BD2/Orden.csv","BD2","Orden"))

'Creamos tablas para base de datos 2'
print("---------Creamos Tabla Usuario---------")
print("Estado Tabla:",j.createTable("BD3","Usuario",8))
print("Estado PKS:",j.alterAddPK("BD3","Usuario",[0]))
print("Estado Inserts",j.loadCSV("./BD3/Personas.csv","BD3","Usuario"))

print("---------Creamos Tabla Privilegio---------")
print("Estado Tabla:",j.createTable("BD3","Privilegio",3))
print("Estado PKS:",j.alterAddPK("BD3","Privilegio",[0]))
print("Estado Inserts",j.loadCSV("./BD3/Privilegios.csv","BD3","Privilegio"))

print("---------Creamos Tabla Acceso---------")
print("Estado Tabla:",j.createTable("BD3","Acceso",2))
print("Estado PKS:", j.alterAddPK("BD3","Acceso",[0,1]))
print("Estado Inserts",j.loadCSV("./BD3/Acceso.csv","BD3","Acceso"))

'Creamos tablas para sistema de peliculas y series'
print("---------Creamos Tabla Pelicula---------")
print("Estado Tabla:",j.createTable("BD4","Pelicula",5))
print("Estado Inserts",j.loadCSV("./BD4/Pelicula.csv","BD4","Pelicula"))

print("---------Creamos Tabla Serie---------")
print("Estado Tabla:",j.createTable("BD4","Serie",5))
print("Estado PKS:", j.alterAddPK("BD4","Serie",[0]))
print("Estado Inserts",j.loadCSV("./BD4/Serie.csv","BD4","Serie"))

print("---------Creamos Tabla Capitulo---------")
print("Estado Tabla:",j.createTable("BD4","Capitulo",5))
print("Estado Inserts",j.loadCSV("./BD4/Capitulo.csv","BD4","Capitulo"))

print("------------------Listado de Tablas de las bases de datos-----------------------")
print("Tablas de BD1:",j.showTables("BD1"))
print("Tablas de BD2:",j.showTables("BD2"))
print("Tablas de BD3:",j.showTables("BD3"))
print("Tablas de BD4:",j.showTables("BD4"))

final = time.time()
print("------------------------------------------------------------------")
print("Tiempo de Ejecucion:", final-inicio, "segundos")