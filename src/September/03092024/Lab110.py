# Take input and create class in python

class person:

    def __init__(self):
        self.name = input("enter the name\n")
        self.age = input("enter the age\n")
        self.phone = input("enter the phone\n")
        self.occupation = input("enter the occupation\n")

    def display_information(self):
            print(f"name is {self.name}")
            print(f"age is {self.age}")
            print(f"phone number is {self.phone}")
            print(f"occupation is {self.occupation}")

# create an object
person1 = person()

# call the display function

person1.display_information()