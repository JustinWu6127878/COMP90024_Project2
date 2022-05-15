import couchdb

db_address = 'http://admin:123456@localhost:5984/'
try:
    couchServer =  couchdb.Server(db_address)
except Exception as e:
    print(e)

task = ['inflation', 'vacc', 'government']

for t in task:
    db_key = t+'_result'
    couchServer.create(db_key)
    res_db = couchServer[db_key]
    for city in ['melb','syd','bris','adel']:
        couchServer.create(t+'_'+city)
        res = {
            'city': city
        }
        res_db.save(res)