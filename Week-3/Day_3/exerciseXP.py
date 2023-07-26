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
    
    def __add0__(self,other):
        return self.amount + other.amount
    
    def __add1__(self):
        self.amount += 5
        return f"{self.amount} {self.currency}"
    
    def __add2__(self,other):
        self.amount += 5
        self.amount += other.amount
        return f"{self.amount} {self.currency}"
    
    def __add3__(self, other):
        if self.currency == other.currency:
           return self.amount + other.amount
        else:
            return f"TypeError: Cannot add between Currency type {self.currency} and {other.currency}"

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
print(c1. __add__())

# >>> c1 + c2
# 15
print(c1. __add0__(c2))

# >>> c1 += 5
# >>> c1
# 10 dollars
print(c1. __add1__())

# >>> c1 += c2
# >>> c1
# 20 dollars
print(c1. __add2__(c2))

# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>
print(c1. __add3__(c3))
