# test_pet.py

from pet import Pet

# Create a test pet
my_pet = Pet(name="Luna", pet_type="cat")

# Test pet actions
print("Initial Status:")
my_pet.get_status()

print("\nFeeding the pet...")
my_pet.eat()

print("\nPlaying with the pet...")
my_pet.play()

print("\nPet takes a nap...")
my_pet.sleep()

print("\nTeaching the pet a new trick...")
my_pet.train("rollover")

print("\nShowing tricks...")
my_pet.show_tricks()

print("\nFinal Status:")
my_pet.get_status()
