import os
def count(file_name):
    vowels_count = 0
    consonants_count = 0
    symbols_count = 0
    f = open(file_name)
    text = f.read()
    for char in text:
        if char.isalpha():
            if char.lower():
                vowels_count += 1
            else:
                consonants_count += 1
        elif not char.isspace():
            symbols_count += 1
                    
    return vowels_count, consonants_count, symbols_count
file_name = "lecture5/read.txt"
s = count(file_name)
print(s[0])
print(s[1])
print(s[2])
