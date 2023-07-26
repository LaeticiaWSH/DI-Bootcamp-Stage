#Ex 1
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
       return f"{self.amount} {self.currency}"
    
    def __int__(self):
        return self.amount
    
    # >>> repr(c1)
    # '5 dollars' 
    def __repr__(self):
        return f"{self.amount} {self.currency}"
    
    def __add__(self):
        return self.amount + 5
    
    def __add__(self,other):
        return self.amount + other.amount

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

# >>> str(c1)
# '5 dollars'
print(c1)

# >>> int(c1)
# 5
print(c1. __int__())

# >>> c1 + 5
# 10
# print(c1. __add__())


print(c1. __add__(c2))