#importing libraries
import streamlit as st
import pandas as pd
import yfinance as yf
import pandas_datareader.data as web
import datetime

import capm_functions

#Streamlit page configuration
st.set_page_config(page_title="CAPM",
                   page_icon="chart_with_upwards_trend",
                   layout='wide')

st.title("Capital Asset Pricing Model")

# getting input from user
try:
    col1, col2 =st.columns([1,1])
    with col1:
        stocks_list = st.multiselect("Choose 4 stocks", ('TSLA','AAPL','NFLX','MSFT','MGM','AMZN','NVDA','GOOGL'),('TSLA','AAPL','AMZN','GOOGL'))

    with col2:
        year=st.number_input("Numbers of years",1,10)

    #downloading data for SP500

    end = datetime.date.today()
    start = datetime.date(datetime.date.today().year-year, datetime.date.today().month, datetime.date.today().day)

    SP500 = web.DataReader(['sp500'], 'fred',start,end)

    stocks_df = pd.DataFrame()

    for stock in stocks_list:
        data = yf.download(stock, period=f'{year}y')
        stocks_df[f'{stock}'] = data['Close']


    stocks_df.reset_index(inplace=True)
    SP500.reset_index(inplace=True)
    SP500.columns = ['Date','SP500']
    stocks_df['Date'] = stocks_df['Date'].astype('datetime64[ns]')
    stocks_df['Date'] = stocks_df['Date'].apply(lambda x:str(x)[:10])
    stocks_df['Date'] = pd.to_datetime(stocks_df['Date'])
    stocks_df = pd.merge(stocks_df, SP500, on='Date', how='inner')

    col1, col2 = st.columns([1,1])
    with col1:
        st.markdown('### Dataframe head')
        st.dataframe(stocks_df.head(), use_container_width=True)

    with col2:
        st.markdown('### Dataframe tail')
        st.dataframe(stocks_df.tail(), use_container_width=True)


    col1, col2 = st.columns([1,1])
    with col1:
        st.markdown('### Price of all the Stocks')
        st.plotly_chart(capm_functions.interactive_plot(stocks_df))


    with col2:
    
        st.markdown('### Price of all the Stocks After Normalization')
        st.plotly_chart(capm_functions.interactive_plot(capm_functions.normalize(stocks_df)))

    stocks_daily_returns = capm_functions.daily_return(stocks_df)
    #print(stocks_daily_returns.head())

    beta = {}
    alpha = {}

    for i in stocks_daily_returns.columns:
        if i !='Date' and i !='SP500':
            b,a = capm_functions.calculate_beta(stocks_daily_returns,i)

            beta[i]=b
            alpha[i]=a
    print(beta, alpha)

    beta_df = pd.DataFrame(columns=['stock','Beta Value'])
    beta_df['Stock'] = beta.keys()
    beta_df['Beta value'] = [str(round(i,2)) for i in beta.values()]


    with col1:
        st.markdown('### Calculated Beta Value')
        st.dataframe(beta_df, use_container_width=True)


    rf = 0
    rm = stocks_daily_returns['SP500'].mean()*252

    return_df = pd.DataFrame()
    return_value = []
    for stock, value in beta.items():
        return_value.append(str(round(rf+(value*(rf-rm)),2)))
    return_df['Stock'] = stocks_list

    return_df['Return value'] = return_value

    with col2:
        st.markdown('### Calculated Return using CAPM')

        st.dataframe(return_df, use_container_width=True)
except:
    st.write('Please select valid Input')




