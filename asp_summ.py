from gensim.summarization import summarize
path='/home/harikrishnan-midhun/Desktop/MainPro/'
def summa(fname):
	#try:
		with open(path+fname+".txt", 'r') as myfile:
			data=myfile.read()#.replace('\n', '.')
			sum1= summarize(data)
			#sum2=summarize(sum1)
			#sum3=summarize(sum2)
	#except:
			#print ""
			#sum1=""
		return sum1

def fwrite(txt,i):
	f= open('/home/harikrishnan-midhun/Desktop/MainPro/Asp_summ/'+i+".txt","w+")
	f.write(txt)

def antiDup(txt):
	ls=txt.split('\n')
	s=set(ls)
	st=''
	for i in s:
		st=st+i+'\n'
	return st


Aspects=['batery','camera','display','performance','price','sound']

for i in Aspects:
	s=summa(i)
	fwrite(antiDup(s),i)
