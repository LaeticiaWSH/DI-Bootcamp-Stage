import pandas as pd
# df = pd.read_csv('my_data.csv')
# print(df)

df = pd.read_csv('store_1_stock.csv')
# print(df)
print(df["Quantity"].sum())
print(df.nlargest(3,"Quantity"))