import couchdb
import nltk
import string
import time
import sys
from collections import defaultdict


# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
for i in ['ha','http','year','month','one','amp','wa','made','inflation']:
    stop_words.add(i)

while(True):
    
    db_address = 'http://admin:123456@172.26.132.252:5984/'
    try:
        couchServer =  couchdb.Server(db_address)
    except Exception as e:
        print(e)

    res_db = couchServer['inflation_result']

    if sys.argv[1] == 'melb':
        db = couchServer['inflation_melb']
        
    elif sys.argv[1] == 'syd':
        db = couchServer['inflation_syd']
        
    elif sys.argv[1] == 'bris':
        db = couchServer['inflation_bris']
        
    elif sys.argv[1] == 'adel':
        db = couchServer['inflation_adel']
        
    else:
        print('wrong argv')
        exit(1)
    
    result_dict = defaultdict(int)

    res_db = couchServer['inflation_result']
    for id in res_db:
        result = res_db[id]
        if result['city'] == sys.argv[1]:
            res_key = id
            latest_id = str(result['latest_id'])
            for key_pair in result['word_list']:
                word = key_pair['name']
                count = key_pair['value']
                result_dict[word] = count
            break
    print('load previous data')

    map_fun = '''function (doc) {
    if (doc.id > '''+latest_id+'''){
        emit(doc.id, doc.processed_text);
    }
}'''
    _doc = {
        "_id": "_design/"+latest_id,
        "views": {
            latest_id: {
                "map": map_fun
            }
        }
    }
    db.save(_doc)
    
    print('map reduce save')
    start_index = 0
    update_id = 0
    print('start update')
    while(True):
        tweet_list = list(db.view('_design/'+latest_id+'/_view/'+latest_id,skip=start_index,limit=1000))
        if tweet_list == []:
            break
        print(start_index)
        for row in tweet_list:
            update_id = max(update_id, row['key'])
            tweet = row['value']
            word_tokens = word_tokenize(tweet)
            for word in word_tokens:
                word = lemmatizer.lemmatize(word.lower())
                if word in stop_words:
                    continue
                for c in string.punctuation:
                    word = word.replace(c,'')
                if word in stop_words:
                    continue
                if len(word) < 2:
                    continue

                result_dict[word] += 1

        start_index += 1000

    word_dict = []
    sort_result = sorted(result_dict.items(), key=lambda x: x[1],reverse=True)
    for name, count in sort_result:
        word_dict.append({'name': name, 'value': count})
    result['latest_id'] = update_id
    result['last_update'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    result['word_list'] = word_dict
    res_db[res_key] = result
    break
    # time.sleep(12*60*60)

