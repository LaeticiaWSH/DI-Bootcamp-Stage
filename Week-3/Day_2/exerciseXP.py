#  Ex 1
class Pets():
    def __init__(self, animals):
       self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
# Bengal = Cat("Lulu",5)
# Chartreux = Cat("Tutu",10)
# Siamese = Cat("Pipi",7)
all_cats =[Bengal("Lulu",5),Chartreux("Tutu",10),Siamese]

sara_pets = Pets(all_cats)
sara_pets.walk()

# Ex 2
class Dog():
    def __init__(self,name,age,weight) :
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print(f"{self.name} is barking.")

    def run_speed(self):
        self.speed = (self.weight / (self.age * 10))
        print(f"\nThe running speed of the dog is {self.speed}")

    def fight(self,other_dog):
        dog1 = (self.weight / (self.age * 10)) * self.weight
        dog2 = (other_dog.weight / (other_dog.age * 10)) * other_dog.weight
        if dog1 > dog2:
            return f"{self.name} won the fight."
        elif dog2 > dog1 :
            return f"{other_dog.name} won the fight."
        else:
            return f"There was a draw."
        
dog_1 = Dog("Felix",13,50) #19.23
dog_2 = Dog("Oli",14,55) #21.60
dog_3 = Dog("Phoenix",6,40) #26.66
dog_1.run_speed()
print(dog_1.fight(dog_2))
print(dog_3.fight(dog_1))
print(dog_2.fight(dog_1))