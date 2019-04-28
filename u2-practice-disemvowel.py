# """
# Unit 2 Practice 2:
# Python Collections - Disemvowel Challenge
# -----------------------------------------

# Goal: remove all the vowels to whatever word we pass in the function.

VOWELS = "aeiou"          

def disemvowel(word):
    letters = list(word)
    for letter in word: 
        if letter.lower() in VOWELS:       
            letters.remove(letter)              
    word = "".join(letters)
    return word

word = input("Enter a word: ")
word = disemvowel(word)
print(word)