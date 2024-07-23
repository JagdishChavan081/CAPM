# CAPM (Capital Asset Pricing Model)
End-To-End Portfolio Project on CAPM(Capital Asset Pricing Model)

## Abstract
web application that is designed to perform CAPM calculations for different stocks. The application uses Python programming language and its libraries such as Pandas, NumPy, Streamlit and Plotly, to gather stock data from Yahoo Finance and perform calculations to determine expected returns.


## Introduction
* CAPM is a model that describes the relationship between the expected return and risk of securities.
* CAPM indicates that the expected rturn on a security is equal to the risk-free return plus risk premium.

## ri = rf + Bi(rm - rf)

**ri** = Expected return on security.
**rf** = Risk free rate of return.
**Bi** = Beta between the stock and the market.
**rm** = Expected return of the market.


## Risk Free Asset Return
* A risk free assest could be a US Government 10 year Treasury bill.
* Investors who are extermely risk risk averse would prefer to buy the risk free asset to protect their money and earn a low return.
* If investors are intrested in gaining more return, they have to bear more risk compared to the risk free asset

## Market Portfolio Return
* Market portfolio includes all securites in the market.  A good representation of the market portfolio is the S&P 500.
* Market portfolio return is the average return of the overall retrun of the SP500

## Beta
* its a measure of a stock risk (volatility of returns)reflected by measuring the flucuation of its price changes relative to the overall market.

β = 0 : No market Sensitivity
β < 1 : Low Market Sensitivity
β = 1 : Same as Market(neutral)
β > 1 : High Market Sensitivity
β < 0 : Negative Market Sensitivity


