import pickle

class details():
    def __init__(self):
        self.name = None
        self.dob = None

data = []

stop = False
while stop == False:
    check = input("Please input your name (enter to end): ")
    if check == "":
        stop = True
    else:
        record = details()
        record.name = check
        record.dob = input("Please input your date of birth: ")
        data.append(record)

with open("textfile3.dat", mode = "wb") as text_file:
    pickle.dump(data, text_file)
