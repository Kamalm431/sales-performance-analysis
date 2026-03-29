from itertools import groupby

import pandas as pd
import matplotlib.pyplot as plt

#loading dataset
df = pd.read_csv("C:/Users/kamal/OneDrive/Desktop/sales.csv")

#first row dataset
print(df.head())

#the total revenue of sales
total_revenue = df["Order ID"].sum()
print("Total Revenue:", total_revenue)

#top 5 products of datatset
top_products = df.groupby("Item Type")["Total Revenue"].sum().sort_values(ascending=False).head(5)
print("Top 5 Products:\n",top_products)

#show monthly sales trends found in the data
df["Ship Date"] = pd.to_datetime(df["Ship Date"])
df["Month"] = (df["Ship Date"]).dt.to_period("M")

monthly_sales =df.groupby("Month")["Total Revenue"].sum()
print("Monthly Sales:\n",monthly_sales)

#visual representation of monthly sales
monthly_sales.plot()
plt.title("Monthly Sales")
plt.show()



