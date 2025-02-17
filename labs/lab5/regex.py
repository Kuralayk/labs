import re
#1
p1 = r'ab*'
str = " abbb abb a ac abbbb"
match = re.findall(p1, str)
print(match)

#2
p2 = r'ab{2,3}'
str2 = "abb abbb abbbb ab a abbb"
match2 = re.findall(p2, str2)
print(match2)

#3
p3 = r'\b[a-z]+_[a-z]+\b'
str3 = "hello_world test_case some_var example_Example"
match3 = re.findall(p3, str3 )
print(match3)

#4
p4 = r'\b[A-Z][a-z]+\b'
str4 = "Hello Worls CASE abs Abc"
match4 = re.findall(p4, str4)
print(match4)

#5
p5 = r'a.*b$'
str5 = ["axb", "a123b", "ab", "acb", "aXYZb", "abbbbc"]
match5 = [s for s in str5 if re.fullmatch(p5, s)]
print(match5)

#6
text = input("Enter a string: ")
result = re.sub(r"[ ,.]", ":", text)
print(result)

#7
def seven(str7):
    words = str7.split('_')
    u = words[0] + ''.join(word.capitalize() for word in words[1:])
    return u
str7 = input("Enter: ")
print(seven(str7))

#8 
str8 = input("enter: ")
words = re.findall(r'[A-Z][a-z]*', str8)
print(words)

#9
str9 = input("Enter string: ")
result = re.sub(r'([A-Z])', r'\1', str9).strip()
print(result)

#10
def ten(str10):
    case = re.sub(r'([A-Z])', r'_\1', str10).lower()
    return case.lstrip('_')

str10 = input("enter a string: ")
print(ten(str10))
