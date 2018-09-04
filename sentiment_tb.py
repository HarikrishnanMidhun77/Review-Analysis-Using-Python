from textblob import TextBlob
import nltk
import sys
reload(sys)
sys.setdefaultencoding('utf8')
path='/home/harikrishnan-midhun/Desktop/MainPro/AspectLevelSumm/'
aspects=['batery','camera','display','performance','price','sound']
def fwrite(txt,fold,pol):
	f= open('/home/harikrishnan-midhun/Desktop/MainPro/pros_and_cons/'+fold+"/"+pol,"w+")
	#f.truncate()
	f.write(txt+"\n")
	
def sentAna(sents,asp):
	posls=[]
	negls=[]
	ps=''
	ns=''
	for i in sents:
		print i+'\n'
		i=i.decode('utf-8').strip()
		blob = TextBlob(i)
		pol=blob.sentiment.polarity
		print pol
		if(pol>float(0.0)):
			posls.append(i)
		elif(pol<float(0.0)):
			negls.append(i)
	print posls
	print "\n\n"
	print negls
	for j in posls:
		ps=ps+j+'\n'
	for k in negls:
		ns=ns+k+'\n'
	print ps+"\n\n"
	print ns
	fwrite(ps,asp,'pros')
	fwrite(ns,asp,'cons')

for asp in aspects:
	#print asp+"\n"
	with open(path+asp, 'r') as myfile:
				text=myfile.read()
				sents = nltk.sent_tokenize(text)
	sentAna(set(sents),asp)

			
		
