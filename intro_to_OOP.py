

#  ATTRIBUTES
# size
#  ears
#  breed
#  color

# METHODS are mostly like functions 
# jumps
# barks
# snuggle 

class Dog:
    #constructor
    def __init__(self, size, ear_size, breed, color): 
        self.size = size
        self.ear_size = ear_size
        self.breed = breed 
        self.color = color
    def bark(self):
        if self.size == "small":
            print("Yip yip!")
        elif self.size == "medium":
            print("Woof woof!")
        else:
            print("BARK! BARK!")

# another CHILD class 

class ServiceDog(Dog):
    def __init__(self, size, ear_size, breed, color):          
        super().__init__(size, ear_size, breed, color) #inherit from the parent class (Dog)
        self.vest = vest

    def turn_on_lights(self):
        print("LIGHTS ON")

jasmines_dog = Dog("medium", "gigantic", "supermutt", "tan" )    

jordy = ServiceDog("medium", "gigantic", "supermutt", "tan", "black")
   # turn on lights
   # glucose levels     

print(jordy.vest)







# jasmines_dog.bark()

# louvelles_dog = Dog("small", "big", "corgi", "tri-color")

# louvelles_dog.bark()