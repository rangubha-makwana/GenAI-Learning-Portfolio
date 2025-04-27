corpus = """Hello Welcome, To Rangubha's Learnign Journey,
Please be part of entrie journey! , to understand it.
"""
print(corpus)

### Tokenization
### Paragraphs  -- > Sentence 
import nltk
nltk.download('punkt')  # Download tokenizer model
nltk.download('punkt_tab')  # Download tokenizer model

from nltk.tokenize import sent_tokenize
a = sent_tokenize(corpus)
print(a)
