from flask import Flask

# __name__ var is automatically set to '__main__' value. It represents the module that is executing the script / API. 
app = Flask(__name__)

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement the speak() method")

# Derived class 1
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Derived class 2
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Flask routes
@app.route('/')
def home():
    return "Welcome to the Animal Sound App!"

@app.route('/animal/<animal_type>/<name>')
def animal_sound(animal_type, name):
    if animal_type.lower() == 'dog':
        animal = Dog(name)
    elif animal_type.lower() == 'cat':
        animal = Cat(name)
    else:
        return "Sorry, we don't have that animal!"

    sound = animal.speak()
    return f"The {animal_type} named {animal.name} says: {sound}"

if __name__ == '__main__':
    app.run()
