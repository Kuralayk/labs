from utilities import reverse_words, is_palindrome , grams_to_ounces

sentence = "We are ready"
print("Reversed sentence:", reverse_words(sentence))

word = "Madam"
print(f"Is '{word}' a palindrome?", is_palindrome(word))

gram_value = 56
ounce_value = grams_to_ounces(gram_value)
print("ounce_value.2f")
