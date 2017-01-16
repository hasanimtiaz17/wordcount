import urllib
webf = urllib.urlopen('http://www.umich.edu/~umfandsf/other/ebooks/alice30.txt')
txt = webf.read()
from collections import Counter
wordcount = Counter(txt.split())
for item in wordcount.items(): print("{},{}".format(*item))




