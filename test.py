class Person:

    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age

    def __str__(self):
        return 'Person name is {self.name} and age is {self.age}'

    def __repr__(self):
        return 'Person(name={self.name}, age={self.age})'


p = Person('Pankaj', 34)

print(p.__str__())
print(p.__repr__())