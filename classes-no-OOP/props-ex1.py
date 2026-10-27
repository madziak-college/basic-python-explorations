# see also: https://realpython.com/python-property/

class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property  # <-- add the `property` built-in
    def name(self):
        return f"{self.first} {self.last}"

john = Person("John", "Doe")
print(john.name)
