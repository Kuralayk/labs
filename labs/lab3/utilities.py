def reverse_words(sentence):
    words = sentence.split()
    return ' '.join(words[::-1])


def is_palindrome(s):
    s = s.replace(" ", "").lower() 
    return s == s[::-1]

def grams_to_ounces(grams):
    ounces = grams / 28.3495231
    return ounces