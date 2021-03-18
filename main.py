
import math
def modules():
  print(math.sin(90))
  newModule.snake()


  #1. Import the math module and call the sin function
#2. Create your own module with the function snake()

class App(object):
  def start(self):
    print('Starting')

class DisApp(object):
  def start(self):
    print("Starting")

class Apple(App):
  def getVersion(self):
    print('Apple version')

class Linux(App, DisApp):
  def getLinuxVersion(self):
    print('Linux version')

    #Inheritance
#1. Create a new class that inherits from the class App
#2. Try to create a class that inherits from two super classes (multiple inheritance)