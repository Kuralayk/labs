#1
def grams_to_ounces(grams):
    ounces = grams / 28.3495231
    return ounces

gram_value = 56
ounce_value = grams_to_ounces(gram_value)
print(f"{gram_value} grams is equal to {ounce_value:.2f} ounces")

#2
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius
fahrenheit_value = 45
celsius_value = fahrenheit_to_celsius(fahrenheit_value)
print(f"{fahrenheit_value} Fahrenheit is equal to {celsius_value:.2f} Celsius")

#3
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (chickens * 2) + (rabbits * 4) == numlegs:
            return chickens, rabbits
    return None, None 

numheads = 35
numlegs = 94
chickens, rabbits = solve(numheads, numlegs)
if chickens is not None:
    print(f"Number of chickens: {chickens}")
    print(f"Number of rabbits: {rabbits}")
else:
    print("No solution found.")

#4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
prime_numbers = filter_prime(numbers)
print("Prime numbers:", prime_numbers)

#5
from itertools import permutations

def print_permutations(s):
    for perm in permutations(s):
        print(''.join(perm))

s = input("Enter a string: ")
print_permutations(s)

#6
def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

s = input("Enter a sentence: ")
print(reverse_words(s))

#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

has_33([1, 3, 3])
has_33([1, 3, 1, 3]) 
has_33([3, 1, 3])
#8
def spy_game(nums):
    code = [0, 0, 7]
    for i in range(len(nums) - 2):
        if nums[i:i+3] == code:
            return True
    return False
spy_game([1,2,4,0,0,7,5]) 
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])

#9
import math
def sphere_volume(radius):
    return (4/3) * math.pi * radius**3
value = 6
result = sphere_volume(value)
print(result)

#10
def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst
result = unique_elements([5,6 , 4 ,4 ,4 ,2 , 6,9,7,5])
print(result)

#11
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
print(is_palindrome("gfyd"))

#12
def histogram(lst):
    for value in lst:
        print('*' * value)
histogram([4,9,7])

#13
import random
def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    number_to_guess = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break
guess_the_number()

#14
