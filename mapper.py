import sys
import string
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip().lower()
    line = line.translate(None,string.punctuation)
    line=line.replace("!", "")
    line=line.replace(",", "") 
    line=line.replace("?", "")
    line=line.replace(";", "")
    line=line.replace("(", "")
    line=line.replace(")", "")
    line=line.replace("-", "")    

# split the line into words
    words = line.split()
    # increase counters
    for word in words:
       
        # Reduce step, i.e. the input for reducer.py
        #
        print '%s\t%s' % (word, 1)
