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

def loading(file_path):
    with open(file_path, 'rb') as f:
        persons = pickle.load(f)
        for person in persons:
            print(person)


persons = [
    Person('ali', 30, 'tehran'),
    Person('reza', 25, 'rasht')
]

dumping('persons.pkl', persons)
loading('persons.pkl')