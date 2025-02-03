#1
class StringProcessor:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Enter a string: ")

    def printString(self):
        print(self.text.upper())
processor = StringProcessor()
processor.getString()
processor.printString()

#2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length ** 2

square = Square(5)
print(square.area()) 
shape = Shape()
print(shape.area())  

#3
class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
rect = Rectangle(5, 3)
print(rect.area())  
shape = Shape()
print(shape.area())

#4
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

p1 = Point(3, 4)
p2 = Point(6, 8)
p1.show()      
p2.show()       
print(p1.dist(p2))  
p1.move(10, 12)
p1.show()   
#5
class Bankaccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = 0
    def deposit(self,amount):
        if amount > 0 :
            self.balance += amount
        return self.balance
    def withdraw (self,amount):
        if 0 < amount <= self.balance :
            self.balance -= amount
        return self.balance
account = Bankaccount("Mia Doe" , 2300)

print(account.deposit(500))
print(account.withdraw(200))
print(account.withdraw(2000))
#6
def prime(n):
    if n < 2 :
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 :
            return True
    return False
numbers = [4, 5 , 7 , 9 , 10, 35 ,12]
pnums = list(filter(lambda x: prime(x), numbers))
print(pnums)
