"""Define a class which has at least two methods: 
1.getString: to get a string from console input 
2.printString: to print the string in upper case."""
'''
class Methods:
  def __init__(self):
    self.s = ''
  def getString(self):
    self.s = input()
  def printString(self):
    print(self.s.upper())
  
s = Methods()
s.getString()
s.printString()
'''
#------------------------------------------------
"""Define a class named Shape and its subclass Square. 
The Square class has an init function which takes a length as argument. 
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
Define a class named Rectangle which inherits from Shape class from task 2. 
Class instance can be constructed by a length and width. 
The Rectangle class has a method which can compute the area."""
'''
class Shape:
  def __init__(self,area=0):
    self.area = area
  def area(self):
    print(self.a)

class Square(Shape):
  def __init__(self,length):
    self.a = length**2

sq1 = Square(2)
sq1.area()

class Rectangle(Shape):
  def __init__(self,length,width):
    self.length = length
    self.width = width
  def area(self):
    print(self.length*self.width)

rec1 = Rectangle(3,5)
rec1.area()
'''
#------------------------------------------------
"""Write the definition of a Point class. Objects from this class should have a
a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points"""
'''
class Point:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def show(self):
    print("Coordinates of a point are x:"+str(self.x)+" and y:"+str(self.y))
  def move(self,x,y):
    self.x = x
    self.y = y
  def dist(self):
    print(int((self.x**2+self.y**2)**0.5))

point1 = Point(5,7)
point1.show()
point1.move(3,4)
point1.dist()
'''
#------------------------------------------------
"""Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. 
Withdrawals may not exceed the available balance. 
Instantiate your class, make several deposits and withdrawals, 
and test to make sure the account can't be overdrawn."""
'''
class Account:
  def __init__(self,name,balance):
    self.owner = name
    self.balance = balance
  def deposit(self,amount):
    self.balance+=amount
    print("Successfully transfered")
  def withdraw(self,amount):
    if amount<=self.balance:
      self.balance-=amount
      print("Please dont forget your card")
    else:
      print("Transaction Error: Exceeds withdrawal limit")

acc1 = Account("Elon Musk",0)
acc1.deposit(10000)
acc1.withdraw(5000)
acc1.withdraw(7000)
'''
#------------------------------------------------
"""Write a program which can filter prime numbers in a list by using filter function. 
Note: Use lambda to define anonymous functions."""
'''
def prime(x):
  if x==1: return False
  for i in range(2,x):
    if x%i==0:
      return False
  return True

l1 = [1,2,3,4,5,6,7,8,9,10]
print (list(filter(prime,l1)))
'''