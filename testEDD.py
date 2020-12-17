# File:         JSON Mode Test File for EDD
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Luis Espino

import Storage  as j

# assume no data exist or execute the next optional drop function
j.dropAll()

# test Databases CRUD
print(j.createDatabase('db1'))      # 0 
print(j.createDatabase('db1'))      # 2
print(j.createDatabase('db4'))      # 0
print(j.createDatabase('db5'))      # 0
print(j.createDatabase(0))          # 1
print(j.alterDatabase('db5','db1')) # 3
print(j.alterDatabase('db5','db2')) # 0
print(j.dropDatabase('db4'))        # 0
print(j.showDatabases())            # ['db1','db2']

# test Tables CRUD
print(j.createTable('db1','tb4',3))     # 0
print(j.createTable('db1','tb4',3))     # 3
print(j.createTable('db1','tb1',3))     # 0
print(j.createTable('db1','tb2',3))     # 0

print(j.alterAddPK('db1','tb1',[0,1]))    # 0
print(j.showTables('db1'))              # ['tb1', 'tb2']
print(j.alterDropPK('db1','tb1'))       # 0
print(j.alterDropPK('db1','tb2'))       # 4