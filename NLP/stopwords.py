import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stopwords = list(stopwords.words("english"))

str = "NLP for social media listening is unique because it understands internet short forms (LOL, BRB, TL;DR), slangs, code-switching, emoticons and emojis, and hashtags. No matter what your customers choose to speak, NLP allows you to extract information from it, and prepare it for an ML model to ingest."

str = str.lower()

wtk = word_tokenize(str)

result = []

for word in wtk:
    if word not in stopwords:
        result.append(word)

print(" ".join(result))