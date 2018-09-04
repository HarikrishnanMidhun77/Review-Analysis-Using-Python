from rouge import Rouge 
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


def antiDup(txt):
	ls=txt.split('\n')
	s=set(ls)
	st=''
	for i in s:
		st=st+i+'\n'
	return st

try:
	path='/home/harikrishnan-midhun/Desktop/MainPro/AspectLevelSumm/display'

	with open('/home/harikrishnan-midhun/Desktop/MainPro/hum_summ', 'r') as myfile:
		hum_summ=myfile.read()
		hls=hum_summ.splitlines()
		for i in hls:
			if i != " ":
				hum_summ=hum_summ+i
	with open(path, 'r') as myfile:
		data=myfile.read()#.replace('\n', '.')
		data=antiDup(data)
		sum1= summarize(data)
	print "\nSummary Using Text Rank\n______________________________\n"
	print sum1
	dic=begin(path)
	s=dictostr(dic)
	s=antiDup(s)
	print "\n\nSummary Using Hybrid TFIDF\n___________________________\n"
	print s
	# print "\nHuman Summary\n______________________________\n"
	# print hum_summ

	rouge = Rouge()
	#scorestf = rouge.get_scores(hum_summ,s)
	#print "\nRouge Score of TFIDF\n____________________________\n"
	#print scorestf

	#scorestr= rouge.get_scores(hum_summ,sum1)
	#print "\nRouge Score of TextRank\n____________________________\n"
	#print scorestr
except:
	print""
