from gensim.summarization import summarize
from my_hydtfidf import begin
import sys
reload(sys)

def dictostr(dic):
	s=''
	li=dic.values()
	for i in li:
		s=s+i+"\n"
	return s

path='/home/harikrishnan-midhun/Desktop/MainPro/AspectLevelSumm/camera'
with open(fname, 'r') as myfile:
	data=myfile.read()#.replace('\n', '.')
	sum1= summarize(data)
print "\nSummary Using Text Rank\n______________________________\n"
print sum1
dic=begin(path)
s=dictostr(dic)
print "\n\nSummary Using Hybrid TFIDF\n___________________________\n"
print s