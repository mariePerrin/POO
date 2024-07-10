class Animal:                           
    def __init__(self, name, weight, size):                     # the new object is initialized
        self.name = name
        self.__weight = weight                                  # private attribute "weight"
        self.size = size

    def get_weight(self):                                       # get the values of private attribute "weight"
        return self.__weight
    
    def set_weight(self, new_weight):                           # set the value of "weight" using an object of a class
        self.__weight = new_weight
        if new_weight > 0:
            self.__weight = new_weight
        else:
            raise ValueError("The weight should be a positive number")

    def se_deplacer(self):
        print("I walk")                                         # pass, if no action is intended


class Serpent(Animal):
    def __init__(self, name, weight, size, hazardous):
        super().__init__(name, weight, size)
        self.hazardous = hazardous


    def se_deplacer(self):
        print("I crawl")


class Oiseau(Animal):
    def __init__(self, name, weight, size, max_altitude):
        super().__init__(name, weight, size)                # overcharge methods form Animal class
        self.max_altitude = max_altitude                    # definition of local variables

    def se_deplacer(self):
        print("I fly")


monkey = Animal(name = "Monkey", weight = 60, size = 90)    # create an object Animal() = instantiate the "class Animal"
python = Serpent(name= "Python", weight = 100, size = 600, hazardous = "yes")
eagle = Oiseau(name = "Eagle", weight = 6.5, size = 200, max_altitude = 6000)


if __name__ == "__main__":

    print(monkey.name, "Weight:", monkey.get_weight(), "kg", "Size:", monkey.size, "cm")        # access the object's attributes
    print(python.name, "Weight:", python.get_weight(), "kg", "Size:", python.size, "cm", "Hazardous:", python.hazardous)
    print(eagle.name, "Weight:", eagle.get_weight(), "kg", "Size:", eagle.size, "cm", "Max_altitude:", eagle.max_altitude, "m")

    monkey.se_deplacer()
    python.se_deplacer()
    eagle.se_deplacer()

    print(isinstance(python, Animal))
    print(issubclass(Oiseau, Animal))

    print(monkey.set_weight(350))





