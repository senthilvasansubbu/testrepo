from collections import Counter
#input
text = "python is great python is powerful and python is popular"

def word_counte(text):
    wordcounts = Counter(text.split())
    wc = dict(wordcounts)
    return wc

wc = word_counte(text)
print(wc)

# without using library Counter
def word_counter(text):
    wordcounts = {}
    words = text.lower().split()
    for word in words:
        wordcounts[word] = wordcounts.get(word, 0) + 1
    return wordcounts

text = "python is great python is powerful and python is popular"
result = word_counter(text)
print(result)

#robust word counter
import re

def word_count(text):
    wordcounts = {}
    words = re.findall(r"\b\w+\b", text.lower())
    for word in words:
        wordcounts[word] = wordcounts.get(word, 0) + 1
    return wordcounts

rresult = word_count(text)
print(rresult)
