import pandas as pd
# series = pd.Series([1,2,3,4]) # IT's one dimension.
# print(series)

# df = pd.DataFrame({ #Dataframe has col and ro 
#    "Name": ["Alice", "Bob", "Charlie"],
#    "Age": [25, 32, 22]
# })
# print(df)
# data = {
#    "fruits": ["apple", "banana", "cherry"],
#    "count": [10, 20, 15]
# }
# df = pd.DataFrame(data)
# print(df)

# series = pd.Series([1, 2, 3, 4])
# print(series)
# #Customize your own index.
# series = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# print(series)

# # #If you don't define something by default it willl be 1,2,3.
# df = pd.DataFrame({
#    "Name": ["Alice", "Bob", "Charlie"],
#    "Age": [25, 32, 22]
# })
# # print(df.iloc[0])
# # print(df.loc['a'])# There was a customize index.
# # print(df.iloc[1:2])
# df['Grade'] = ['A', 'B', 'C']
# print(df)

# print("2023")
# df["Age"]= df["Age"] + 1
# print(df)




# df.to_csv('my_data.csv', index=False)

#EX 1
# series = pd.Series([20,30,15,10], index = ["Apples","Bananas","Cherries","Dates"])
# print(series,"\n")

# #EX 2
df = pd.DataFrame({
    "Quantity": [20,30,15,10],
    "Color": ["Red","Yellow","Red","Brown"],
    "Price per kg": [3,2,4,5]
}, index = ["Apples","Bananas","Cherries","Dates"])
print(df)

df.to_csv('store_1_stock.csv')




