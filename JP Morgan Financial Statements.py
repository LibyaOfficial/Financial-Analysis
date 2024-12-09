#!/usr/bin/env python
# coding: utf-8

# In[7]:


import yfinance as yf
import pandas as pd

# Ticker symbol for JPMorgan Chase & Co.
ticker = 'JPM'

jpm = yf.Ticker(ticker)

# Retrieve financial statements
balance_sheet = jpm.balance_sheet
income_statement = jpm.financials
cash_flow_statement = jpm.cashflow

# Transpose the dataframes for better readability
balance_sheet = balance_sheet.T
income_statement = income_statement.T
cash_flow_statement = cash_flow_statement.T

# Display the financial statements
print("Balance Sheet:")
print(balance_sheet)
print("\nIncome Statement:")
print(income_statement)
print("\nCash Flow Statement:")
print(cash_flow_statement)

#Save the financial statements to Excel files
balance_sheet.to_excel('JPM_balance_sheet.xlsx')
income_statement.to_excel('JPM_income_statement.xlsx')
cash_flow_statement.to_excel('JPM_cash_flow_statement.xlsx')


# In[ ]:




