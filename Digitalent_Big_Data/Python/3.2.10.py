﻿# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input()
user_word = user_word.upper()
vowels = 'AIUEO'

for letter in user_word:
    # Complete the body of the for loop.
    if letter in vowels :
        continue
    print(letter)