from __init__ import *

# Download the words corpus
nltk.download('words')  

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
        # Get a list of similar words and suggest them to the user
        words = set(nltk.corpus.words.words())
        similar_words = get_close_matches(word, words, n=5, cutoff=0.7)
        if similar_words:
            print(f"No definition found for '{word}'. Did you mean:")
            for i, similar_word in enumerate(similar_words):
                print(f"{i+1}. {similar_word}")
            print()
        else:
            print(f"No definition found for '{word}'. Please try again.\n")
