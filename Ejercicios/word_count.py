'''
EXERCISE: Print all the ocurrences of every character in a string
'''

str_ = "This is an awesome occasion. This has never happened before."

char_ocurrances = dict()

# dict.get(char, 0)  -> default is 0
# it initializes first the dictionary with 0 values and keeps adding one

for char in str_:
    char_ocurrances[char] = char_ocurrances.get(char, 0) + 1

print(char_ocurrances)

word_ocurrances = dict()

for word in str_.split():
    word_ocurrances[word] = word_ocurrances.get(word, 0) + 1

print(word_ocurrances)
