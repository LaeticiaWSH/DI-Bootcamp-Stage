
# #Daily Challenge 1
word = input('Enter a word : ')
a = word.lower()
dict = {x : [] for x in a}   #creates dict with keys being unique values in a
for i,x in enumerate(a):
    dict[x].append(i) 

print(dict)

#  #Daily Challenge 2
items_purchase1 = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

# Expected output if wallet = "$300"
 #["Bread", "Fertilizer", "Water"]

items_purchase2 = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

#Expected output if wallet = "$100" 
# ["Apple", "Bananas", "Fan", "Honey", "Pan", "Spoon"]

items_purchase3 = {
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}

# Expected output if wallet = "$1" 
#"Nothing"

item_purchasedNo = int(input("Enter the items_purchased your interested in (1-3): "))

if 0 < item_purchasedNo < 4:
    if item_purchasedNo == 1:
      items_purchased = items_purchase1
    elif item_purchasedNo == 2:
      items_purchased = items_purchase2
    else:
      if item_purchasedNo == 3:
        items_purchased = items_purchase3
  

my_wallet = int(input("Enter the amount in your wallet: "))
can_afford = []

for item, price in items_purchased.items():
   item_price = int(price.replace("$","").replace(",",""))
   if item_price <= my_wallet:
      can_afford.append(item)
if can_afford != []:
  can_afford = sorted(can_afford)   
  print(can_afford)
else:
   print("You can afford Nothing.")

