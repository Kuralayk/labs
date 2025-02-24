import math
#1`
def list(nums):
    return math.prod(nums)

nums = [2, 3, 4, 5]
result = list(nums)
print(result)

#2
def letters(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count
text = "Hello WorlD"
upper, lower = letters(text)
print("upper:", upper," lower:" ,lower)

#3
def palindrome(s):
    return s == s[::-1]
word = "madam"
print(palindrome(word))

#4
import time 
def sqrt(number, delay):
    time.sleep(delay / 1000)
    return math.sqrt(number)
num = 25100
delay = 2123
result = sqrt(num, delay)
print(result)

#5
def five(tup):
    return all(tup)

values = (True, True , 1, "hello")
print(five(values))