
from textblob import TextBlob
import nltk
path='/home/harikrishnan-midhun/Desktop/MainPro/'
aspects=['batery','camera','display','performance','price','sound']
posper=float(0)
negper=float(0)
def fwrite(asp,t,pos,neg):
	#try:
		posper=(float(pos)/t)*100
		negper=(float(neg)/t)*100
		f= open('/home/harikrishnan-midhun/Desktop/MainPro/report/perc_report',"a+")
		#f.truncate()
		f.write("\n\n"+asp+"\n------------------------------\nTotal number of Reviews	on "+asp+"	:	"+str(t)+'\n'+" Number of Positive Reviews	:	"+str(pos)+"\nNumber of negative Reviews	:	"+str(neg)+"\n Percentage of positive reviews	:	"+str(posper)+"\n Percentage of negative reviews	:	"+str(negper))
	#except:
		#print"error"
def sentAna(sents,asp):
		#try:
			t=0
			pos=0
			neg=0
			for i in sents:
				#print i+'\n'
				t=t+1
				i=i.decode('utf8')
				#print i+'\n'
				blob = TextBlob(i)
				pol=blob.sentiment.polarity
				#print pol
				if(pol>float(0.0)):
					pos=pos+1
				elif(pol<float(0.0)):
					neg=neg+1
				#print t,pos,neg
			fwrite(asp,t,pos,neg)
		#except:
			#print "Exception"
		
			

	
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
	
for asp in aspects:	
	sents=lsmake(path+asp+".txt")
	sentAna(set(sents),asp)
