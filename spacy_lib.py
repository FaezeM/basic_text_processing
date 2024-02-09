import spacy
from collections import Counter

text = "An operating system (OS) is system software that manages computer" \
"hardware and software resources, and provides common services for" \
"computer programs. Time-sharing operating systems schedule tasks " \
"for efficient use of the system and may also include accounting " \
"software for cost allocation of processor time, mass storage, " \
"peripherals, and other resources. For hardware functions such as " \
"input and output and memory allocation, the operating system acts " \
"as an intermediary between programs and the computer hardware, " \
"although the application code is usually executed directly by the " \
"hardware and frequently makes system calls to an OS function or is " \
"interrupted by it. Operating systems are found on many devices that " \
"contain a computer – from cellular phones and video game consoles to " \
"web servers and supercomputers."

example_string = "Il Lusitania era stato colpito e stava affondando rapidamente, mentre le barche venivano lanciate a tutta velocità. Le donne e i bambini erano in fila in attesa del loro turno. Alcuni si aggrappavano ancora disperatamente a mariti e padri. Una ragazza era sola, leggermente in disparte dal resto."

example_str = "Jenny ran away and started swimming towards the US coast."

def get_words(str):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(str)
    return [token.text for token in doc]

def get_sent(str):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(str)
    return [sent.text for sent in doc.sents]

def repeated_words(str):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(str)
    tokens = [token.text for token in doc]
    word_count = Counter(tokens)
    return [word for word, count in word_count.items() if int(count) > 1]

def word_counts(str):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(str)
    tokens = [token.text for token in doc]
    word_count = Counter(tokens)
    return word_count

def it_lang_counts(str):
    nlp = spacy.load("it_core_news_sm")
    doc = nlp(str)
    tokens = [token.text for token in doc]
    word_count = Counter(tokens)
    return word_count

def find_verbs(str):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(str)
    return [token.text for token in doc if token.pos_ == 'VERB']

def find_person(str):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(str)
    return [ent.text for ent in doc.ents if ent.label_ == 'PERSON']


print(find_person(example_str))