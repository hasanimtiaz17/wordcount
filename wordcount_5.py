import sys
import string
import pandas as pd
import urllib

pre = str(raw_input('Define your prefix: '))
url = str(raw_input('What is the URL of the text file: '))
webf = urllib.urlopen(url)
txt = webf.read().lower()
txt=txt.translate(None, string.punctuation)
txt=txt.replace("!", "")
txt=txt.replace(",", "")
txt=txt.replace("?", "")
txt=txt.replace(";", "")
txt=txt.replace("(", "")
txt=txt.replace(")", "")
txt=txt.replace("-", "")
from collections import Counter
wordcount = Counter(txt.split())

df=pd.DataFrame(wordcount.items())
df.columns = ['word', 'count']

for i in range(len(df)):
	if df['word'][i].startswith(pre)==True:
		print '%s,%s' % (df['word'].iloc[i],df['count'].iloc[i])

