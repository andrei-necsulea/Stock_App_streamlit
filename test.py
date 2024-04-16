import pandas as pd


def stock_tickers():
 frame = pd.read_excel("tickers_all.xlsx" , sheet_name="Tickers")
 stock_list = frame['Stocks'].to_list()
 return stock_list

def etf_tickers():
 frame = pd.read_excel("tickers_all.xlsx" , sheet_name="Tickers")
 etf_list = frame['ETF'].to_list()
 return etf_list

def futures_tickers():
 frame = pd.read_excel("tickers_all.xlsx" , sheet_name="Tickers")
 ftr_list = frame['Futures'].to_list()
 return ftr_list

def index_tickers():
 frame = pd.read_excel("tickers_all.xlsx" , sheet_name="Tickers")
 index_list = frame['Indexes'].to_list()
 return index_list

def mutual_funds_tickers():
 frame = pd.read_excel("tickers_all.xlsx" , sheet_name="Tickers")
 mtf_list = frame['MTF'].to_list()
 return mtf_list

def currency_tickers():
 frame = pd.read_excel("tickers_all.xlsx" , sheet_name="Tickers")
 currency_list = frame['Currency'].to_list()
 return currency_list
