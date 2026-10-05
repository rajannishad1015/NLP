import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

text = "text normalisation is an essential step"
text = text.lower()
text = text.translate(str.maketrans('', '', string.punctuation))
tokens = word_tokenize(text)
stop_words = set(stopwords.words('english'))
print(tokens)

filtered_tokens = []
for word in tokens:
    if word not in stop_words:
        filtered_tokens.append(word)
print(filtered_tokens)

stemmer = PorterStemmer()
stemmed_tokens = []
for token in filtered_tokens:
    stemmed_tokens.append(stemmer.stem(token))
print(stemmed_tokens)

lemmatizer = WordNetLemmatizer()
lemmatized_tokens = []
for token in stemmed_tokens:
    lemmatized_tokens.append(lemmatizer.lemmatize(token))
print(lemmatized_tokens)
