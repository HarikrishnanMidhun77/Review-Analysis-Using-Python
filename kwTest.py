from gensim.summarization import keywords
path='/home/harikrishnan-midhun/Desktop/MainPro/pros_and_cons/'
aspects=['batery','camera','display','performance','price','sound']



def kw(asp,pol):
	with open(path+asp+"/"+pol, 'r') as myfile:
				data=myfile.read()#.replace('\n', '.')
				kw=keywords(data)
				print "\n\n"+i+"\t\t:"+pol+"\n_______________________\n"+kw

for i in aspects:
	kw(i,"pros")
	kw(i,"cons")