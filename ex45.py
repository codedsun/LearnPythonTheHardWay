##Animal is-a object
class Animal(object):
    pass

##Dog is a object
class Dog(Animal):

     def __init__(self,name):
         ##initializing name
         self.name = name

##Cat is a object
class Cat(Animal):

    def __init__(self, name):
        ##Initializing name
        self.name = name
        
## person is an object
class Person(object):

    def __init__(self, name):
        self.name = name
        self.pet = None

##
class Employee(Person):

    def __init__(self, name, salary):
        super(Employee,self).__init__(name)
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

rover = Dog("Rover")

satan = Cat("Satan")

marry = Person("Marry")
marry.pet = satan

frank= Employee("Frank",120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()

        
        
        
        
    
