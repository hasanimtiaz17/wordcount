import sys
txt = sys.stdin.read()
from collections import Counter
wordcount = Counter(txt.split())
for item in wordcount.items(): print("{},{}".format(*item))
