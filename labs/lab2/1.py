a = 200
b = 33

if b > a :
    print("b is greater thah a")
else :
    print("b is not greater than a")

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

x = 200
print(isinstance(x,int))