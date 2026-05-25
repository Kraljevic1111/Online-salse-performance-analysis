import pandas as pd 

sales = [
    {"order_id": 1, "customer": "Ana", "city": "Beograd", "category": "Fitness", "price": 500, "quantity": 1, "date": "2024-01-05"},
    {"order_id": 2, "customer": "Marko", "city": "Novi Sad", "category": "Running", "price": 120, "quantity": 2, "date": "2024-01-12"},
    {"order_id": 3, "customer": "Ana", "city": "Beograd", "category": "Fitness", "price": 700, "quantity": 1, "date": "2024-02-01"},
    {"order_id": 4, "customer": "Jelena", "city": "Niš", "category": "Cycling", "price": 900, "quantity": 1, "date": "2024-02-10"},
    {"order_id": 5, "customer": "Petar", "city": "Novi Sad", "category": "Running", "price": 80, "quantity": 3, "date": "2024-03-01"},
    {"order_id": 6, "customer": "Ivana", "city": "Beograd", "category": "Cycling", "price": 1000, "quantity": 1, "date": "2024-03-15"},
    {"order_id": 7, "customer": "Marko", "city": "Novi Sad", "category": "Fitness", "price": 600, "quantity": 1, "date": "2024-03-20"},
    {"order_id": 8, "customer": "Ana", "city": "Beograd", "category": "Running", "price": 150, "quantity": 2, "date": "2024-04-01"},
    {"order_id": 9, "customer": "Petar", "city": "Novi Sad", "category": "Fitness", "price": 550, "quantity": 1, "date": "2024-04-10"},
]

#kreiranje df  and EDA

df = pd.DataFrame(sales)
print(df.head())
print(df.info())
print(df.describe())
print(df.dtypes)
print(df.isna().sum())

#dodavanje kolone revenue 

df['revenue'] = df['price'] * df['quantity']

#pretvaranje date u datetime

df['date'] = pd.to_datetime(df['date'])

#dodavanje kolone mesec

df['month'] = df['date'].dt.month

#ukupan revenue 

total_revenue = df['revenue'].sum()
print('Total revenue:',total_revenue)

#average order value
avg_order_value = df['revenue'].mean()
print('Average order value:',avg_order_value)

#Najbolji kupac po revenue
top_customer_by_revenue = df.groupby('customer')['revenue'].sum().sort_values(ascending=False).head(1)
print('Top customer by revenue:',top_customer_by_revenue)

#najbolja kategorija po revenue
top_category_by_revenue = df.groupby('category')['revenue'].sum().sort_values(ascending = False).head(1)
print('Top category by revenue:',top_category_by_revenue)

#top grad po revenue
top_city_by_revenue = df.groupby('city')['revenue'].sum().sort_values(ascending=False).head(1)
print('Top city by revenue:',top_city_by_revenue)

#kupci koji iamju vise od jedne porudzbine

customers_orders = df.groupby('customer')['order_id'].count().sort_values(ascending = False)
customers_with_more_than_one_order =customers_orders[customers_orders>1]
print('Customers_with_more_than one order:',customers_with_more_than_one_order)

#revenue po customeru
revenue_per_customer = df.groupby('customer')['revenue'].sum().sort_values(ascending = False)
print('Revenue per customer:',revenue_per_customer)

#broj porudzbina po customeru
number_of_orders_by_customer = df.groupby('customer')['order_id'].count().sort_values(ascending = False)
print('Number of orders by customer:',number_of_orders_by_customer)

#revenue po kategoriji 
revenue_per_category = df.groupby('category')['revenue'].sum().sort_values(ascending = False).reset_index()
print('Revenue per category:',revenue_per_category)

#quantity sold po kategoriji

quantity_sold_per_category = df.groupby('category')['quantity'].sum().sort_values(ascending = False)
print('Quantity sold per category:',quantity_sold_per_category)

#avergae revenue po kategoriji

avg_revenue_per_category = df.groupby('category')['revenue'].mean()
print(' Average Revenue per category:',avg_revenue_per_category)

#revenue po mesecima 

revenue_per_month = df.groupby('month')['revenue'].sum().reset_index()
print('Revenue per month:',revenue_per_month)

#broj porudzbina po mesecu

num_of_orders_per_month = df.groupby('month')['order_id'].count()
print('Number of orders per month:',num_of_orders_per_month)

#visualization bar chart revenue po kategoriji

import matplotlib.pyplot as plt
import seaborn as sns 

plt.figure(figsize=(10,6))
sns.barplot(data = revenue_per_category,x = 'category',y = 'revenue',color = 'skyblue')
plt.title('Revenue per category')
plt.xlabel('Category')
plt.ylabel('Revenue')
plt.show()


#revenue po mesecima lineplot

plt.figure(figsize=(10,6))
sns.lineplot(data = revenue_per_month, x= 'month',y = 'revenue',marker = "o",color = 'blue')
plt.title('Revenue per Month')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.grid(True)
plt.show()

# heatmap corretlation beewen price,qunatity,revenue

df_corr = df[['price','quantity','revenue']].corr()

sns.heatmap(df_corr,annot= True,cmap = 'Greens',fmt = ".1f")
plt.title('Correlation matrix')
plt.show()

#boxplot revenue 

plt.figure(figsize=(10,6))
sns.boxplot(data = df, x= 'category', y = 'revenue',hue = 'category',palette = 'Set2')
plt.title('Revenue per category')
plt.show()