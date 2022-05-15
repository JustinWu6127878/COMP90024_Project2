import couchdb
import time
import logging

logging.basicConfig(level=logging.DEBUG #设置日志输出格式
                    ,stream=sys.stdout
                    ,format="%(asctime)s - %(name)s - %(levelname)-9s - %(filename)-8s : %(lineno)s line - %(message)s" #日志输出的格式
                    # -8表示占位符，让输出左对齐，输出长度都为8位
                    ,datefmt="%Y-%m-%d %H:%M:%S" 
                    )

while(True):
    db_address = 'http://admin:123456@172.26.132.252:5984/'
    try:
        couchServer =  couchdb.Server(db_address)
    except Exception as e:
        print(e)
    logging.info('Update vacc')
    db = couchServer['vacc_result']
    db_list = ['vacc_melb', 'vacc_syd', 'vacc_bris', 'vacc_adel']

    for id in db:
        res = db[id]
        city = res['city']
        logging.info('updating ' + city)
        city_db = couchServer['vacc_'+city]
        result = list(city_db.view('_design/sentiment/_view/sentiment',group=True))
        for row in result:
            res[row.key] = row.value
        db[id] = res
        logging.info('success')

    logging.info('updating government')
    db = couchServer['government_result']
    db_list = ['government_melb', 'government_syd', 'government_bris', 'government_adel']

    for id in db:
        res = db[id]
        city = res['city']
        logging.info('updating ' + city)
        city_db = couchServer['government_'+city]
        result = list(city_db.view('_design/created_at/_view/date',group=True))
        date_list = []
        for row in result:
            out = {}
            if row.key in ['May 12', 'May 11', 'May 13']:
                continue
            out[row.key] = row.value
            date_list.append(out)
        res['date_list'] = date_list
        db[id] = res
        logging.info('success')
    logging.info('update finish! wait')
    time.sleep(12*60*60)