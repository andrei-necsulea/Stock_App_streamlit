#this is the function module
#assuming that I have to set a type of chart which will be "line-chart"
#importing yfinance for manipulation and visualization of their data

import yfinance as yf
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from sqlalchemy import create_engine


plt.style.use('dark_background')
matplotlib.rcParams['backend'] = 'TkAgg'

engine = create_engine("postgresql://postgres:fdc2E3BB6eDF2Dcc351b5dC6acCaB5DD@roundhouse.proxy.rlwy.net:23113/railway")
connection = engine.connect()

data = pd.read_sql_table("tickers" , connection)

def retrieve_data(column_name):
 rtr_list = data[column_name].to_list()
 rtr_list_copy = []
 for i in rtr_list :
    if i != 'NULL' :
        rtr_list_copy.append(i)
 return rtr_list_copy

    
def ticker_data(data_list):
   ticker = yf.Ticker(data_list[2])
   Asset = pd.DataFrame(yf.download(ticker, start=data_list[0],end=data_list[1])['Adj Close'])     
   return Asset

def live_chart(chart_dataframe , type_of_chart):
   match type_of_chart :
      case 'line' :
         st.line_chart(chart_dataframe , color='#0b7c30')
      case 'area' :
         st.area_chart(chart_dataframe , color='#0b7c30')
      case 'bar'  :
         st.bar_chart(chart_dataframe , color='#0b7c30')