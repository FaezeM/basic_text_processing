import nltk
from collections import Counter

example_string = "IT was 2 p.m. on the afternoon of May 7, 1915. The Lusitania had been struck and was sinking rapidly, while the boats were being launched with all possible speed. The women and children were being lined up awaiting their turn. Some still clung desperately to husbands and fathers. One girl stood alone, slightly apart from the rest. She was quite young, not more than eighteen. She did not seem afraid, and her grave, steadfast eyes looked straight ahead."

def word_list(str):
    return nltk.word_tokenize(str)

def sent_set(str):
    return set(nltk.sent_tokenize(str))

def find_duplicate_words(str):
    words = nltk.word_tokenize(str)
    word_count = Counter(words)
    li = [word for word, count in word_count.items() if count > 1]
    return li

def count_dict(str):
    words = nltk.word_tokenize(str)
    word_count = Counter(words)
    print(word_count)

#find_duplicate_words(example_string)
count_dict(example_string)