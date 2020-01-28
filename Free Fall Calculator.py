#python 3.7.1
##Coded by Krypt0N

#Import math for square root
import math
#This is just a welcome message!
def welcome():
  print("Please select a option from above:")

##This creates a menu wich is the base of the program
def menu0():
  print("")
  print("1) Calculate velocity, gravity and time (v, g and t)")
  print("2) Calculate impact velocity, gravity and height (v, g and h)")
  print("3) Calculate path, gravity and time (s, g and t)")
  choice = input()
  if choice == "1":
    menu1()
  elif choice == "2":
    menu2()
  elif choice == "3":
    menu3()
  else:
    print("Incorrect Option. Try Again!")

##This menu helps to know a variable from two given 
def menu1():
  welcome()
  print("1) Calculate v (velocity)")
  print("2) Calculate g (gravity aceleration)")
  print("3) Calculate t (time)")
  print("")
  option = input()
  if option == "1" :
    velocity()
  elif option == "2":
    gravity()
  elif option == "3":
    time()
  else: 
    print("Incorrect Option, Try Again!")
    
def velocity():
  gravity = float(input("Please enter the gravity value (m/s^2):"))
  time = float(input("Please enter the time value (s):"))
  velocity = (gravity * time)
  print("The Velocity Is:", velocity, "m/s")

def gravity():
  velocity = float(input("Please enter the velocity value (m/s):"))
  time = float(input("Please enter the time value (s):"))
  gravity = (velocity / time)
  print("The Gravity Value Is:", gravity, "m/s")

def time():
  velocity = float(input("Please enter the velocity value (m/s):"))
  gravity = float(input("Please enter the gravity value (m/s^2):"))
  time = (velocity / gravity)
  print("The Time Is:", time, "s")

##The same...
def menu2():
  welcome()
  print("1) Calculate v (impact velocity)")
  print("2) Calculate g (gravity aceleration)")
  print("3) Calculate h (height)")
  print("")
  option = input()
  if option == "1":
    impact()
  elif option == "2":
    newtons_baby()
  elif option == "3":
    height()
  else: 
    print("Incorrect Option, Try Again!")

def impact():
  gravity = float(input("Please enter the gravity value (m/s^2):"))
  height = float(input("Please enter the height value (m):"))
  impactv = math.sqrt(2 * gravity * height)
  print("The Velocity Is:", impactv, "m/s")

def newtons_baby():
  impactv = float(input("Please enter the impact velocity value (m/s):"))
  height = float(input("Please enter the height value (m):"))
  gravity = (impactv ** 2) / (2 * height)
  print("The Gravity Is:", gravity, "m/s^2")

def height():
  impactv = float(input("Please enter the impact velocity value (m/s):"))
  gravity = float(input("Please enter the gravity value (m/s^2):"))
  height = (impactv ** 2) / (2 * gravity)
  print("The Height Is:", height, "m")

##The same.....
def menu3():
  welcome()
  print("1) Calculate s (path lenght)")
  print("2) Calculate g (gravity aceleration)")
  print("3) Calculate t (time)")
  option = input()
  if option == "1":
    path()
  elif option == "2":
    gravedad()
  elif option == "3":
    measure()
  else: 
    print("Incorrect Option, Try Again!")

def path():
  gravity = float(input("Please enter the gravity value (m/s^2):"))
  time = float(input("Please enter the time value (s):"))
  path = (0.5 * gravity * time)
  print("The Path Lenght Is:", path, "m")

def gravedad():
  path = float(input("Please enter the path lenght value (m):"))
  time = float(input("Please enter the time value (s):"))
  gravity = (2 * path) / (time ^2)
  print("The Gravity Value Is:", gravity, "m/s^2")

def measure():
  path = float(input("Please enter the path lenght value (m):"))
  gravity = float(input("Please enter the gravity value (m/s^2):"))
  time = math.sqrt((2*path) / (gravity))
  print("The Time Is:", time, "s")

##This is the order of execution of the program. All is conected together to menu0()
print("Welcome to the Krytp0N's Free Fall Calculator")
welcome()
menu0()
