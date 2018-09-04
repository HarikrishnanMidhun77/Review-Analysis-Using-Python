from gensim.summarization import summarize
import glob
import os
from my_hydtfidf import begin
path='/home/harikrishnan-midhun/Desktop/MainPro/sub_aspects/'
def dictostr(dic):
	s=''
	li=dic.values()
	for i in li:
		s=s+i+"\n"
	return s
def summa(fname):
	try:
		with open(fname, 'r') as myfile:
			data=myfile.read()#.replace('\n', '.')
			sum1= summarize(data)
			#sum2=summarize(sum1)
			#sum3=summarize(sum2)
	except:
			print ""
			sum1=""
	return sum1

def fwrite(txt,i):
	f= open('/home/harikrishnan-midhun/Desktop/MainPro/AspectLevelSumm/'+i,"w+")
	f.write(txt)

subAspects=['batery','camera','display','performance','price','sound']

for i in subAspects:
	aspSumm=''
	for filename in os.listdir(path+i):
		#print path+i+'/'+filename
		dic=begin(path+i+'/'+filename)
		s=dictostr(dic)
		aspSumm=aspSumm+"\n"+s
		#print "\n\n\n"+aspSumm
		#aspSumm=summarize(aspSumm)
	fwrite(aspSumm,i)
	

