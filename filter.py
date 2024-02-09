import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

stop_words = stopwords.words('italian')
example_string = "Il Lusitania era stato colpito e stava affondando rapidamente, mentre le barche venivano lanciate a tutta velocità. Le donne e i bambini erano in fila in attesa del loro turno. Alcuni si aggrappavano ancora disperatamente a mariti e padri. Una ragazza era sola, leggermente in disparte dal resto."

# full_text = example_string.lower() # not lowercasing any more
word_tokens = nltk.word_tokenize(example_string)
print (word_tokens[:20])
filtered_tokens = [w for w in word_tokens if w.casefold() not in stop_words]
print (filtered_tokens[:20])