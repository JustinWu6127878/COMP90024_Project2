import couchdb


map_fun = "function (doc) { var words = doc.created_at.split(' '); emit(words.slice(0, 3).join(' '));}"

_doc = {
    "_id": "_design/created_at",
    "views": {
        "date": {
            "map": map_fun,
            "reduce": "_count"
        }
    }
}

db_address = 'http://admin:123456@172.26.132.252:5984/'

try:
    couchServer =  couchdb.Server(db_address)
except Exception as e:
    print(e)


db_list = ['government_melb', 'government_syd', 'government_bris', 'government_adel']

for db_key in db_list:
    db = couchServer[db_key]
    db.save(_doc)
    