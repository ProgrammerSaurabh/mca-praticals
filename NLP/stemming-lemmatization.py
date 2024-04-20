import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

str = "NLP for social media listening is unique because it understands internet short forms (LOL, BRB, TL;DR), slangs, code-switching, emoticons and emojis, and hashtags. No matter what your customers choose to speak, NLP allows you to extract information from it, and prepare it for an ML model to ingest."

str = str.lower()

wtk = word_tokenize(str)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

stemmerResult = []
lemmatizerResult = []

for word in wtk:
    stemmerResult.append(stemmer.stem(word))
    lemmatizerResult.append(lemmatizer.lemmatize(word))

print("Original: " + " ".join(wtk) + "\n")
print("Stemmed: " + " ".join(stemmerResult) + "\n")
print("Lemmatized: " + " ".join(lemmatizerResult) + "\n")