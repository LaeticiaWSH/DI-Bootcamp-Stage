
# #Daily Challenge 1
# word = input('Enter a word : ')
# a = word.lower()
# dict = {x : [] for x in a}   #creates dict with keys being unique values in a
# for i,x in enumerate(a):
#     dict[x].append(i) 

# print(dict)

#  #Daily Challenge 2
items_purchase = {
  "Water": '$1',
  "Bread": '$3',
  "TV": '$1,000',
  "Fertilizer": '$20'
}
# mapped_dict = {key :value.strip('$') for key,value in items_purchase()}
# print(mapped_dict)
# # def convert_to_int(v):
#     result = [dict([v, int(x)] for k, v in items_purchase.items())]
#     return result

# # list = []
# wallet = (input('Enter the money you have $$ = '))
# # # price = items_purchase1.values.replace('$','')
# # # items_purchase = [{k : int(v) for k, v in items_purchase1.items()}]
# def update(v):
for k,v in items_purchase.items():
        price = (v.strip('$'))
        items_purchase[k] = (price)
print(items_purchase)
#items_purchase = {k : int(v) for k, v in items_purchase.items()}
#         print(v)
#x = map(update([k, int(v)] for k, v in items_purchase.items()))
# #     v = v.replace('$','')
# #     price = convert_to_int(v)
# #     print(type(price))
# print(x)
# # #     if wallet > price :
# # #         list.append(k)
# # print(list)

