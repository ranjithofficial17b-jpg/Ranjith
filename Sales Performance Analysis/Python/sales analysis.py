import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("sales_data_500.csv")
print(df.head())
print(df.info())
print(df.isnull().sum())
print("Duplicate rows:",df.duplicated().sum())

df['Gross sales']=df['Quantity']*df['Unit Price']
df['Total cost']=df['Quantity']*df['Cost']
df['Profit']=df['Gross sales']-df['Total cost']
df['profit margin']=df['Profit']/df['Gross sales']
print(df.head())

top_products = df.groupby("Product")["Gross sales"].sum().sort_values(ascending=False)
print(top_products.head())

regional_sales=df.groupby('Region')['Gross sales'].sum().sort_values(ascending=False)
print(regional_sales)

df['Date']=pd.to_datetime(df['Date'])
df['Month']=df['Date'].dt.to_period('M')
monthly_sales=df.groupby('Month')['Gross sales'].sum().sort_values(ascending=False)
print(monthly_sales)

'''monthly_sales_chart=df.groupby('Month')['Gross sales'].sum()
monthly_sales_chart.plot(kind='line',marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

top_5=(df.groupby('Product')['Gross sales']
       .sum()
       .sort_values(ascending=False)
       .head(5)
)
top_5.plot(kind='bar')
plt.title('Top 5 Product by sales')
plt.xlabel('Product')
plt.ylabel('sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()'''

'''regional_sales=(df.groupby('Region')['Gross sales'].sum().sort_values(ascending=False))
regional_sales.plot(kind='bar')
plt.title('Regional Sales Performance')
plt.xlabel('Region')
plt.ylabel('Gross sales')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()'''

monthly_profit=(df.groupby('Month')['Profit'].sum().sort_values(ascending=False))
print(monthly_profit)

monthly_profit_chart=df.groupby('Month')['Profit'].sum()
monthly_profit_chart.plot(kind='bar')
plt.title('monthly profit analysis')
plt.xlabel('Month')
plt.ylabel('Profit')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

