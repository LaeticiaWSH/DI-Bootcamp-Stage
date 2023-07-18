# print("Hello world\n" * 4,"I love python\n" * 4)
valid = False
while valid == False:
    print("Enter a month between 1(January) and 12(December) :")
    month=int(input())
    if month < 1 or month > 12:
        valid = True
    if month >= 3 and month <= 5:
        print("The season is Spring")
    elif month >= 6 and month <= 8:
        print("The season is Summer")
    elif month >= 9 and month <= 11:
        print("The season is Autumn")
    else:
       print("The season is winter")


