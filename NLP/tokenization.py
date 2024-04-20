import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize, sent_tokenize

str = "NLP for social media listening is unique because it understands internet short forms (LOL, BRB, TL;DR), slangs, code-switching, emoticons and emojis, and hashtags. No matter what your customers choose to speak, NLP allows you to extract information from it, and prepare it for an ML model to ingest."

str = str.lower()

wtk = word_tokenize(str)
stk = sent_tokenize(str)

print(wtk)
print(stk)
