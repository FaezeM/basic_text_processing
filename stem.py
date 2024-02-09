from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

example_string = "The Lusitania had been struck and was sinking rapidly, while the boats were being launched with all possible speed."

def P_stem(str):
    port_stm = PorterStemmer()
    words = word_tokenize(example_string)
    stemmed_words = [port_stm.stem(word) for word in words]
    print(stemmed_words)