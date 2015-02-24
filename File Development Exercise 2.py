import pickle

class details():
    def __init__(self):
        self.name = None
        self.dob = None

with open("textfile3.dat", mode = "rb") as text_file:
    people = pickle.load(text_file)
    for person in people:
        print(person.name)
        print(person.dob)
