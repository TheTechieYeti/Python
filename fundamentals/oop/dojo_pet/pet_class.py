class Pet:
    def __init__(self, name, type, tricks, health = 100, energy = 100):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
    
    def sleep(self):
        if self.pet.energy > 100:
            print(f"{self.pet.name} can't fall asleep! Maybe try doing an activity with him? ")
            
        else:
            self.pet.energy =+ 30
            print(f"{self.pet.name}'s health is {self.pet.health}.")
        return self

    def eat(self,):
        print(f"{self.pet.name} ate something.")
        self.pet.energy += 5
        self.pet.health += 10
        return self

    def play(self,):
        self.pet.health += 5
        self.pet.energy -= 10
        print(f"{self.pet.name}'s health is {self.pet.health}.")
        return self

    def noise(self,):
        print(f"{self.pet.name} barked.")
    
    def attributes(self,):
        attributes_statement = f"{self.pet.name}'s attributes are: \n Health: {self.pet.health} \n Energy: {self.pet.energy}"
        return attributes_statement

class Pet_cat(Pet):
    def __init__(self, name, type, health=100, energy=100, spay=True):
        super().__init__(name, type, health, energy, spay)
        self.spay = spay
    
