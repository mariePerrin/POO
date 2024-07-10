from Animal import Animal, Serpent, Oiseau                          # import inputs from Animal.py

class Zoo:                           
    def __init__(self, animals: list[Animal]):                      # attribut which is a list of objetcs of type "Animal"
        self.animals = []                                           # empty list for future storage of animals
        for animal in animals:                                      # for each index, we retrieve the name of the animal
            self.add_animal(animal)


    def add_animal(self, animal: Animal):                           # adding an object of type Animal to an Zoo instance
        if isinstance(animal, Animal):
            self.animals.append(animal)
        else:
            raise TypeError("It should be an animal")


    def __str__(self):                                              # by calling the function str, is returned one string
        msg = f"This zoo contains {len(self.animals)} animals:\n"   # which defines the obkect explicitly
        for animal in self.animals:
            msg += f"{animal.name}\n"
        return msg
    

    def __add__(self, other_zoo):
        return Zoo(self.animals + other_zoo.animals)


monkey = Animal(name = "Monkey", weight = 60, size = 90)    # create an object Animal() = instantiate the "class Animal"
python = Serpent(name= "Python", weight = 100, size = 600, hazardous = "yes")
eagle = Oiseau(name = "Eagle", weight = 6.5, size = 200, max_altitude = 6000)
lion = Animal(name = "Lion", weight = 250, size = 250)
panda = Animal(name = "Panda", weight = 160, size = 150)
anaconda = Serpent(name= "Anaconda", weight = 70, size = 300, hazardous = "yes")


if __name__ == "__main__":

    z1 = Zoo([monkey, python, eagle])
    print(z1.animals[2].name)                   # returns the size of the animal with index 2 in the list
    z1.add_animal(lion)                         # add an animal that is not present in the initial list

    print(str(panda))                           # <Animal.Animal object at 0x7fdfe9628f50> (class name and object's memory location)

    for animal in z1.animals:
        print(animal.name)
    print(len(z1.animals))
    print("===========================================")
    print(z1)

    z2 = Zoo([])
    z2.add_animal(lion)
    z2.add_animal(panda)
    z2.add_animal(anaconda)

    z3 = z1 + z2
    print(z3)
