from PyDictionary import PyDictionary

dictionary = PyDictionary()

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
