
class Pet:
    def __init__(self, name, pet_type, hunger=0, energy=5, happiness=5):
        self.name = name
        self.type = pet_type
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness
        self.tricks = []
        self.toys = self.get_toys_by_type()
