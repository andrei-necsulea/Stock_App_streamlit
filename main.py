import streamlit as st
import base64
from functions import *


@st.cache_data
def get_img_as_base64(file):
  with open (file, "rb") as f:
   data = f.read()
  return base64.b64encode(data).decode()

img = get_img_as_base64("bg.jpg")
page_bg_img = f"""
<style>
html,body{{
  font-size: 22px;
}}

[data-testid="stMarkdownContainer"] p{{
  font-size:26px;
}}

[data-testid = "stButton"] {{
margin-top:5%;
display:flex;
justify-content : center;
align-items: center;

}}

[data-testid="stAppViewContainer"] {{
background-image: url("data:image/png;base64, {img}");
background-size: cover;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64, {img}");
background-position: center;
}}

#MainMenu {{visibility: hidden;}} footer {{visibility: hidden;}} 

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("FastAlyze Visualizer STOCK MARKET APP - VSMA")
start_range = st.date_input('Start range : ' )
stop_range = st.date_input('Stop range : ')
select_domain = st.selectbox("Select domain Ticker : " , options=['Stocks' , 'ETF' , 'Futures' , 'Indexes' , 'Mutual Funds' , 'Currency'])


param = str(select_domain)
match param :
   case 'Stocks' :
     select_ticker = st.selectbox("Select Ticker : " , options = retrieve_data('stocks'))  
   case 'ETF' :
     select_ticker = st.selectbox("Select Ticker : " , options = retrieve_data('etf'))  
   case 'Futures' :
     select_ticker = st.selectbox("Select Ticker : " , options = retrieve_data('futures'))  
   case 'Indexes' :
     select_ticker = st.selectbox("Select Ticker : " , options = retrieve_data('indexes'))  
   case 'Mutual Funds' :
     select_ticker = st.selectbox("Select Ticker : " , options = retrieve_data('mutual_funds'))  
   case 'Currency':
     select_ticker = st.selectbox("Select Ticker : " , options = retrieve_data('currency'))  

select_chart_type = st.selectbox("Select chart type : " , options=['Line' , 'Bar' , 'Area'])     

def generate_live_chart_func():
  take_data = [str(start_range) , str(stop_range) , str(select_ticker)]
  match select_chart_type :
    case 'Line':
     live_chart(ticker_data(take_data) , 'line')
    case 'Bar' :
      live_chart(ticker_data(take_data) , 'bar')
    case 'Area' :
      live_chart(ticker_data(take_data) , 'area')

generate_live_chart = st.button("Generate live chart" , on_click=generate_live_chart_func)