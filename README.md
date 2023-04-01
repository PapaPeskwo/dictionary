## Description
This is a simple dictionary app designed for convenient use while reading. You can keep the app running in the background, and whenever you come across a word that you want to look up, simply use the app to get its definition. The app will then save the word and its definition to a CSV file for future reference. This way, you can easily build your own vocabulary list while reading without interrupting your flow.

## Installation

We need the PyDictionary library, which is a Python wrapper for the WordNet lexical database, which is a large lexical database of English words and their meanings.
```
pip install pydictionary 
```

If an error is produced, try:

```
python -m pip install --upgrade pip setuptools
```

And if the issue persists, try:
```
pip install -e git+https://github.com/yeahwhat-mc/goslate#egg=goslate
```
If you had to do all these three steps, you might have to do the first command again:
```
pip install pydictionary
```
We also need to install nltk (The Natural Language Toolkit), which is a Python library for working with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for tasks such as tokenization, stemming, tagging, parsing, and semantic reasoning.
```
pip install nltk
```

## Running the program
(For Windows) open up a terminal and type:
```
py dictionary.py
```
