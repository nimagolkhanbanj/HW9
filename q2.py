import pickle

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"

def dumping(file_addres, persons):
    with open(file_addres, 'wb') as f:
        pickle.dump(persons, f)

