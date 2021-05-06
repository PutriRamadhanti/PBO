#parent class
class Person(object):
    
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

#child class
class Employee(Person):
   def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        #invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

#creation of an object variable or an istance
a = Employee('Rahul', 886012, 200000, "Intern")

#calling a function of the class Person uing itss instance
a.display()

#Putri Ramadhanti
