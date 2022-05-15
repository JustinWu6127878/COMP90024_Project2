from cmath import log
import couchdb
import nltk
import string
import time
import sys
import logging
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
for i in ['ha','http','year','month','one','amp','wa','made']:
    stop_words.add(i)
logging.basicConfig(level=logging.DEBUG #设置日志输出格式
                    ,stream=sys.stdout
                    ,format="%(asctime)s - %(name)s - %(levelname)-9s - %(filename)-8s : %(lineno)s line - %(message)s" #日志输出的格式
                    # -8表示占位符，让输出左对齐，输出长度都为8位
                    ,datefmt="%Y-%m-%d %H:%M:%S" 
                    )


while(True):
    logging.info('start updating')
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
    
    logging.info('get view')
    result_dict = defaultdict(int)
    max_len = len(db)
    start_index = 0
    while(start_index < max_len):
        logging.info(start_index)
        # print(start_index)
        tweet_list = list(db.view('_all_docs',skip=start_index,limit=3000,include_docs=True))
        for row in tweet_list:
            if 'design' in row.doc['_id']:
                continue
            tweet = row.doc['processed_text']
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
                if word == 'inflation':
                    continue
                result_dict[word] += 1
        start_index += 3000
    logging.info('get res_key')
    res_db = couchServer['inflation_result']
    for id in res_db:
        result = res_db[id]
        if result['city'] == sys.argv[1]:
            res_key = id
            break

    logging.info('update result')
    word_dict = []
    sort_result = sorted(result_dict.items(), key=lambda x: x[1],reverse=True)
    for name, count in sort_result[:100]:
        word_dict.append({'name': name, 'value': count})
    result['last_update'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    result['word_list'] = word_dict
    res_db[res_key] = result
    logging.info('update finish, wait')
    time.sleep(12*60*60)
    

