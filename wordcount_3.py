import sys
import string
txt = sys.stdin.read().lower()
txt=txt.translate(None, string.punctuation)
from collections import Counter
wordcount = Counter(txt.split())
for item in wordcount.items(): print("{},{}".format(*item))