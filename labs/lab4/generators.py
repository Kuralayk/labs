def square(N):
    for n in range(1, N + 1):
        yield n ** 2
N = int(input("enter: "))
sq = square(N)

for s in sq:
    print(s)

#2
def even_numbers(n):
    for num in range(0, n + 1, 2): 
        yield num
n = int(input("Enter a number: "))
first = True
for num in even_numbers(n):
    if first:
        print(num, end="")
        first = False
    else:
        print(",", num, end="")
print()

#3
def divide(n):
    for i in range (0,n+1):
        if i % 3 == 0 and i % 4 == 0 :
            yield i
n = int(input("Enter number: "))
for num in divide(n):
    print(num)

#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

a = int(input("a: "))
b = int(input("b: "))
for num in squares(a,b):
    print(num)

#5
def countdown(n):
    for i in range(n, -1, -1):
        yield i 
n = int(input("number: "))
for num in countdown(n):
    print(num)