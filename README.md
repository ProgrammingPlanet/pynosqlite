## PyNoSQLite - Fast and Lightweight json file based database

### getting started - install

```
$ pip3 install pynosqlite
```

### basic usage
```
from pynosqlite import PyNoSQLite

file = 'abc.json'

db = PyNoSQLite(file=file)

#insert single record/document -> return id of the inserted item
id = db.insert({'name': 'robin', 'age': 10})

#insert multiple records/documents -> return List of ids of the inserted items
ids = db.insert_many([{'name': 'asher', 'age': 5}, {'name': 'gush', 'age': 8}])

#get all records -> return dictionary of all records
results = db.all()

#find by id/primary key -> return record dictionary if found else return None
result = db.find(id) #return robin's record

#search for a record -> not implemented yet --TODO--
result = db.search({'name': 'asher'})

#delete single record by id -> return id of deleted item
deleted_id = db.delete(id) #delete robin's record

#delete many records by ids -> return ids of successfully deleted items
deleted_ids = db.delete_many(ids) #delete asher's, gush's records
```


