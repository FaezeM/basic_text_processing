import nltk
from nltk.tokenize import word_tokenize

example_string = "The Lusitania had been struck and was sinking rapidly, while the boats were being launched with all possible speed."
example_str = "While Ann was coming home, Jess went to Spain with Joy and his new Apple laptop."

def find_verb(str):
    words = word_tokenize(str)
    pos_list = nltk.pos_tag(words)
    li = [word for word, pos in pos_list if pos.startswith('VB')]
    return li

def find_persons(str):
    words = word_tokenize(str)
    pos_list = nltk.pos_tag(words)
    li = [word for word, pos in pos_list if pos in ['NNP' , 'NNPS']]
    print(li)

#print(find_verb(example_string))
find_persons(example_str)