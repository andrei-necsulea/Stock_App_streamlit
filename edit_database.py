import psycopg2 as dbm
from test import *
#import concurrent.futures

'''
stocks = stock_tickers()
etf = etf_tickers()
ftr = futures_tickers()
indexes = index_tickers()
mtf = mutual_funds_tickers()
currency = currency_tickers()


tickers = []
for i in range(len(stocks)):
    tickers.append([ stocks[i] , etf[i] , ftr[i] , indexes[i] , mtf[i] , currency[i] ])

for i in range(len(tickers)):
   for j in range(len(tickers[i])):
      if type(tickers[i][j])  == float:  
         tickers[i][j] = 'NULL'

for i in range(len(tickers)):
   tickers[i] = tuple(tickers[i])     

'''
conn = dbm.connect(database="railway", user="postgres", password="fdc2E3BB6eDF2Dcc351b5dC6acCaB5DD", host="roundhouse.proxy.rlwy.net", port="23113")
cursor = conn.cursor()


'''
def into_db(elements):
    sql_command = "INSERT INTO tickers \n VALUES {};"
    cmd = sql_command.format(elements)
    cursor.execute(cmd)

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(into_db, tickers))

print("Succesfully!")    
'''

sql_command = "ALTER TABLE tickers \n DROP COLUMN nr;"
cursor.execute(sql_command)

conn.commit()
cursor.close()
conn.close()