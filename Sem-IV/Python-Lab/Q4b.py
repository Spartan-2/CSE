# Develop a python program to count all the occurrences of vowels, consonants and digits from the given text using Regular expressions

import re

def count(text):

    vowel_pattern = r'[aeiouAEIOU]'
    digit_pattern = r'\d'

    vowel = re.findall(vowel_pattern,text)
    digit = re.findall(digit_pattern,text)

    return len(vowel),len(digit),(len(text)-len(vowel)-len(digit))

txt = input("Enter the text ")
vo,d,co = count(txt)

print(vo,co,d)