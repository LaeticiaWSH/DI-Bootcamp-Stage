from exerciseXP import Dog
from random import randint
        
class PetDog(Dog):
    def __init__(self, name, age, weight):
        Dog.__init__(self,name, age, weight)
        self.trained = False

    def train(self):
        Dog.bark(self)
        self.trained = True
        print (f"{self.name} trained : {self.trained}")

    def play(self,*args):
        
        print(f"{','.join(args)} are all together.")

    def do_a_trick(self,l1):
        if self.trained == True:
            data1 = l1[randint(0,len(l1)-1)]
            print(self.name,data1)


l1 = [" does a barrel roll"," stands on his back legs"," shakes your hand"," plays dead"]
dog = ['Felix','Oli','Phoenix','Elias']
dog_1 = PetDog("Felix",13,50)
dog_2 = PetDog("Oli",14,55)
dog_3 = PetDog("Phoenix",6,40)
dog_4 = PetDog("Elias",12,44)
dog_4.train()
dog_4.do_a_trick(l1)
dog_1.play('Felix',' Oli',' Phoenix',' Elias')
