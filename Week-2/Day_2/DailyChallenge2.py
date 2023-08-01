import datetime
d = int(input("Enter day of birth : "))
m = int(input("Enter month of birth : "))
y = int(input("Enter year of birth : "))
dob = str(d) + " " + str(m) + " " + str(y)
dob = dob.split(" ")
print("D-O-B in format MM-DD-YYYY: %s-%s-%s" % (dob[0],dob[1],dob[2]))
print("D-O-B in format MM/DD/YYYY: %s/%s/%s" % (dob[0],dob[1],dob[2]))
today = datetime.date.today()
year = today.strftime("%Y")
age = int(year) - y
#print(age)

def last_digit(age):
    age_str = str(age)
    last_digit_age = int(age_str[-1])
    return last_digit_age

candle = last_digit(age)
#print(candle)

c = ""
for x in range(0,candle):
    c += "i"

#print(c)
def cake(candle):
    if candle < 2:
        print(f"    _____{c}_____")
    elif 1 < candle < 4:
        print(f"    ____{c}____")
    elif 3 < candle < 6:
        print(f"    ___{c}___")
    elif 5 < candle < 8:
        print (f"    __{c}__")
    else:
        print(f"    _{c}_")

    print(f"   |:H:a:p:p:y:|")
    print(f" __|___________|__")
    print(f"|^^^^^^^^^^^^^^^^^|")
    print(f"|:B:i:r:t:h:d:a:y:|")
    print(f"|                 |")
    print(f"~~~~~~~~~~~~~~~~~~~")

if y % 4 == 0:
    cake(candle)
    cake(candle)
else:
    cake(candle)