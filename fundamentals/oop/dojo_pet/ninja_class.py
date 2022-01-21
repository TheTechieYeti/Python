### Things I still want to do in this file. 
    #1) Have the owner make the pet perform a trick and access it from the tricks list in pet attributes and give him a treat
    #2) Have the owner teach the pet a new trick and import that trick into the pets attributes 

import pet_class
class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self):
        pet_class.Pet.play(self)
        print(f"{self.first_name} took {self.pet.name} for a walk.")
        print(pet_class.Pet.attributes(self))
        return self
    
    def feed(self,):
        pet_class.Pet.eat(self)
        #I'm calling a method from another class. Can I use a parameter from Ninja class and pass it through as my argument for the other class method?
        print(pet_class.Pet.attributes(self))
        return self

    def bathe(self):
        pet_class.Pet.noise(self)
        return self  ### Why do I have to pass through self here? Shouldn't it inherit it? 

    def sleep(self):
        pet_class.Pet.sleep(self)
        print(pet_class.Pet.attributes(self))


# brutus = Pet('Brutus', 'St. Bernard', ['sit', 'fetch', 'play dead'], 80, 50)
scott = Ninja('Scott', 'Elliott', 'biscuits', 'kibble', pet_class.Pet('Brutus', 'St. Bernard', ['sit', 'fetch', 'play dead'], 80, 100))

katie = Ninja('Katie', 'Elliott', 'cat-nip', 'friskys', pet_class.Pet('Sophie', 'Unknown', 80, 100))

# scott.feed().bathe().sleep()
# katie.feed().bathe().sleep()
print(scott.pet.name)
print(katie.pet.spayed)
