import re
from collections import Counter
import codecs
import operator

# Read the whole text.
text = codecs.open("20151231-nyc.txt",'r',"utf-8").read()

#break into single words
words = re.findall(r'\w+', text)
words = [word.lower() for word in words]

#remove words
stopwords= open(r'stopwords.txt', 'r').read().splitlines()
def clean(ws):
    
    #keep only english words
    ws= [x for x in ws if x.isalpha()]
    
    #remove all punctuations
    ws= [x for x in ws if len(x)>3]
    
    #remove all stop words
    ws= [x for x in ws if not x in stopwords]
    
    #add combined words
    ws0 = ws
    ws= ws + [ws[i]+' '+ws[i+1] for i in range(len(ws)-1)]
    ws= ws + [ws0[i]+' '+ws0[i+1] + ' ' + ws0[i+2] for i in range(len(ws0)-2)]

    
    return ws

cleaned_text = clean(words)


word_counts = Counter(cleaned_text)

c = dict(word_counts)

#sorted_c = sorted(c.items(), key=operator.itemgetter(1),reverse = True)
sorted_c = sorted(c, key=c.get,reverse = True)

top = sorted_c[:30]



print ("the top 30 frequent words are:")
for x in top:
    print (x, ": ", c[x])
