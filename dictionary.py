import os
from PyDictionary import PyDictionary

dictionary = PyDictionary()

filename = 'word_definitions.csv'
if not os.path.isfile(filename):
    # Create the file if it does not exist
    open(filename, 'w').close()

while True:
    word = input("Enter a word (or type 'q' to exit): ")
    if word == 'q':
        break
    try:
        meaning = dictionary.meaning(word)
        definition = meaning['Noun'][0]
        if word in open('word_definitions.csv').read():
            print(f'{word}: {definition}\n')
        else:
            with open('word_definitions.csv', 'a') as file:
                file.write(f'{word},{definition}\n')
            print(f'{word}: {definition}\n')
    except (TypeError, KeyError):
        print(f"No definition found for '{word}'. Please try again.\n")
