#EX 1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
        # print(f" The cat name is {self.name} and age is {self.age} year old")

cat_1 = Cat("Felix",9)
cat_2 = Cat("Ana", 4)
cat_3 = Cat("Jewel",7)

def Oldest(list):
    old_cat = list[0]
    for cats in list:
        if cats.age > old_cat.age:
            old_cat = cats
        return old_cat
calculation = Oldest([cat_1,cat_2,cat_3])
print(f"The oldest cat is {calculation.name} age {calculation.age} year old.")

#EX 2
class Dog:
    def __init__(self,name,height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        x = self.height * 2
        print(f"{self.name} jumps {x}cm high!\n")

davids_dog = Dog("Rex",50)
davids_dog.bark()
davids_dog.jump()
sarahs_dog = Dog("Teacup",20)
sarahs_dog.bark()
sarahs_dog.jump()

def bigger(list):
    D1 = list[0]
    D2 = list[1]
    if D1.height > D2.height:
        return D1
    else:
        return D2

comparison = bigger([davids_dog,sarahs_dog])
print(f"The bigger dog is",comparison.name)

#EX 3
class Song:
    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for x in range(len(self.lyrics)):
            piece = self.lyrics[x]
            print(piece)

stairway= Song(["There's a lady who's sure","all that glitters is gold", "and she's buying a stairway to heaven"])
stairway.sing_me_a_song()
#Ex 4
class zoo :
    def __init__(self,zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self,new_animal):
        #valid_animal =0
        for x in range(len(self.animals)):
            if new_animal != self.animals[x]:
                #valid_animal =+ 1
        #if valid_animal == len(self.animals) - 1 :
                self.animals.append(new_animal)
                list(dict.fromkeys(self.animals))

    def get_animals(self):
        print(f"The list of animals: {self.animals}")

    def sell_animal(self,animal_sold):
        for x in range(len(self.animals)):
            if animal_sold == self.animals[x]:
                self.animals.pop(self.animals[x])

    def sort_animals(self):
        sorted_list = sorted(self.animals)
        print(sorted_list)
zoo_info = zoo("zootopia")
zoo_info.add_animal("zebra")
zoo_info.add_animal("lion")
zoo_info.add_animal("elephant")
zoo_info.get_animals()


