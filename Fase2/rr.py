lista = [1,'texto codificado',True]
import zlib
# truncate(database)
for x in lista:
    if type(x) == str:
        i = lista.index(x)
        lista[i] = zlib.compress(x.encode('utf8'),2).hex()
    # insert(database, table, x) 
print(lista)

# truncate(database)
for x in lista:
    if type(x) == str:
        i = lista.index(x)
        lista[i] = zlib.decompress(bytes.fromhex(x)).decode('utf8')
    # insert(database, table, x) 
print(lista)