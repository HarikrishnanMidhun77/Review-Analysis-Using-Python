from gensim.summarization import summarize
import re
path='/home/harikrishnan-midhun/Desktop/MainPro/AspectLevelSumm/'
aspects=['batery','camera','display','performance','price','sound']
def fwrite(txt,fold,pol):
	f= open('/home/harikrishnan-midhun/Desktop/MainPro/pros_and_cons2/'+fold+"/"+pol,"w+")
	f.write(txt)
	
def antiDup(txt):
	ls=txt.split('\n')
	s=set(ls)
	st=''
	for i in s:
		st=st+i+'\n'
	return st
def summ(fold,pol):
	with open('/home/harikrishnan-midhun/Desktop/MainPro/pros_and_cons/'+fold+"/"+pol,"r+")as myfile:
		data=myfile.read()#.replace('\n', '.')
		wlen= len(re.findall(r'\w+', data))
		sum1=antiDup(data)
		while(wlen>500):
			sum1= summarize(sum1)
			wlen= len(re.findall(r'\w+', sum1))
		fwrite(sum1,fold,pol)
		
aspects=['batery','camera','display','performance','price','sound']
pols=['pros','cons']
for i in aspects:
	for j in pols:
		summ(i,j)
		
