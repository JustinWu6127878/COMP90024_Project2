import couchdb

_doc = {
    "_id": "_design/sentiment",
    "views": {
        "sentiment": {
            "map": "function(doc) { emit(doc.sentiment); }",
            "reduce": "_count"
        }
    }
}

db_address = 'http://admin:123456@localhost:5984/'

try:
    couchServer =  couchdb.Server(db_address)
except Exception as e:
    print(e)


db_list = ['vacc_melb', 'vacc_syd', 'vacc_bris', 'vacc_adel']

for db_key in db_list:
    db = couchServer[db_key]
    db.save(_doc)
    