import yfinance as yf
import streamlit as st
from PIL import Image

st.title("Stock Exchange")

image = Image.open('stofck-market.jpg')

st.image(image, use_column_width=True, caption='Stock Exchange', channels="RGB")

st.markdown("""
## **ქართული კომპანიების აქციების შესახებ ინფორმაცია**


""")

#Compaies List with yahoo ticker
CompanyList = {'TBC Bank - Group':'TBCG.L','Bank of Georgia - Group':'BDGSF'}
SelectedCompany = st.selectbox('კომპანია',list(CompanyList.keys()))
TickerSymbol = CompanyList.get(SelectedCompany)
#get data on this ticker
TickerData = yf.Ticker(TickerSymbol)
#get the historical prices for this ticker
TickerDf = TickerData.history(period='1d', start='2010-5-31', end='2020-5-31',)
# Get Line Charts

if SelectedCompany == 'TBC Bank - Group':
    imageSelected = Image.open('tbc-group-small-custom.png')
else:
    imageSelected = Image.open('logo.png')

st.image(imageSelected, use_column_width=True, caption='Stock Exchange', channels="RGB")

st.write("""
### დახურვის ფასები
""")
st.line_chart(TickerDf.Close)

st.write("""
### მოცულობა
""")
st.line_chart(TickerDf.Volume)
