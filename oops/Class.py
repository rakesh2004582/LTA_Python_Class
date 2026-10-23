#OOps is the programining pradigm that orgnaize the software around the data(attributes) and the behavior(methods) that , rather than logic and functions. In oops, that attribute and the method are bundled together as a single unit called class. 

# Class -> Class ia a blueprint or a template for creating objects . It define the attributes and methods of the object . and in the class attribute and methods are bundled together as a single unit . 

# Object- > object is an instance of a class. it is a real world entity that has state and behaviour. 

# Constructor -> Constructor is a special method that is used to initialize the object of a class. it called automatically when an object is created . 

#Slef -> self is a referenec to the current instance of the class. it is used to access the attribute and methods of the class in python . 

 

class Animal:
    state="Up"
    def __init__(self,name,age): # this is the constructor method that is used to initialize the object of the class .
        self.name=name
        self.age=age

    def sound(self):
        print("Crying")

Dog=Animal("Max",3)
print(Dog.name)
print(Dog.age)
Dog.sound()
print(Animal.state)

