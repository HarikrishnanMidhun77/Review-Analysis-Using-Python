from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import gensim
from gensim import corpora
import re
from nltk.corpus import wordnet

rootpath='/home/harikrishnan-midhun/Desktop/MainPro/'
sndfl=open(rootpath+'sound.txt', 'a') 
camfl=open(rootpath+'camera.txt', 'a') 
batfl=open(rootpath+'batery.txt', 'a') 
disfl=open(rootpath+'display.txt', 'a') 
perfl=open(rootpath+'performance.txt', 'a') 
prifl=open(rootpath+'price.txt', 'a') 

def lsmake(path):
	abls=[]
	with open(path) as fp:
   		line = fp.readline()
		while line:
	       		#print("Line {}: {}".format(cnt, line.strip()))
	       		if(not(line.isspace())):
	       			abls.append(line.strip()+".");
	       		line = fp.readline()
	return abls
	
ab=lsmake(rootpath+'sound.txt')
revstr="".join(ab)
print "\n\n"
print revstr
print "\n\n"


stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()
def clean(doc):
    stop_free = " ".join([i for i in revstr.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

doc_clean = [clean(revstr).split()]
dictionary = corpora.Dictionary(doc_clean)
print "\n\n"
print doc_clean
print "\n\n"


doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
Lda = gensim.models.ldamodel.LdaModel
ldamodel = Lda(doc_term_matrix, num_topics=3, id2word = dictionary, passes=100)
a=(ldamodel.print_topics(num_topics=3, num_words=3))
print a
print "\n\n"
strli= [x[1] for x in a]
strli=u"".join(strli)
nums=re.findall('\d*\.?\d+', str(strli))
nums=[float(x) for x in nums]
words=re.findall('[a-zA-Z]+[0-9]?[a-zA-Z]*',str(strli))
Z = [x for _,x in sorted(zip(nums,words),reverse=True)]
seen = set()
topics= []
for item in Z:
    if item not in seen:
        seen.add(item)
        topics.append(item)


		    
def  syns(word):
 	a=set()
 	for syn in wordnet.synsets(i):
		for l in syn.lemmas():
		    a.add(l.name())
	return a

synonyms=[]
for i in topics:
	synonyms.append(syns(i))

print nums
print words
print "\n\n"


print(Z) 
print topics
print "\n\n"



print "\n"	
for i in list(synonyms):
	print i
#print([set(synonyms)])

