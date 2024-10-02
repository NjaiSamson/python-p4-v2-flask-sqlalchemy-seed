#!/usr/bin/env python3
#server/seed.py
from random import choice as rc
from faker import Faker

from app import app
from models import db, Pet

with app.app_context():
    
    fake = Faker()
    
    # Clearing the db for each seeding
    Pet.query.delete()

    # Create an empty list
    pets = []
    
    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']
    
    for names in range(20):
        pet = Pet(name=fake.first_name(),species=rc(species))
        pets.append(pet)

    # Add some Pet instances to the list
    # pets.append(Pet(name = "Fido", species = "Dog"))
    # pets.append(Pet(name = "Whiskers", species = "Cat"))
    # pets.append(Pet(name = "Hermie", species = "Hamster"))
    # pets.append(Pet(name = "Slither", species = "Snake"))
    # pets.append(Pet(name = "Mouse", species = "Dog"))

    # Insert each Pet in the list into the database table
    db.session.add_all(pets)
    print("Seeded successifuly")

    # Commit the transaction
    db.session.commit()