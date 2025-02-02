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
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Adds money to the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws money if there are sufficient funds."""
        if amount > self.balance:
            print("Insufficient funds! Withdrawal denied.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrawn: ${amount}. New balance: ${self.balance}")
        else:
            print("Withdrawal amount must be positive.")

    def show_balance(self):
        """Displays the current balance."""
        print(f"Account Owner: {self.owner}, Balance: ${self.balance}")

account = BankAccount("Alice", 100)

account.show_balance()   
account.deposit(50)      
account.withdraw(30)     
account.withdraw(200)   
account.show_balance()   
#6
def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

numbers = [2, 3, 4, 5, 10, 13, 17, 20, 23, 29, 30]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers:", prime_numbers)
