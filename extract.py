import csv
import re
from itertools import islice
c=0
rootpath='/home/harikrishnan-midhun/Desktop/MainPro/'
pr=open(rootpath+'phone_reviews.txt', 'w+') 
ls=[]
with open('Amazon_Unlocked_Mobile.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if(row['Brand Name']=='Nokia'):
			ls.append(row['Reviews'])
sentenceEnders = re.compile('[.!?]')#(r'''(?<=[.!?]['"\s])\s*(?=[A-Z])''')
for i in ls[:3000]:
		sentenceList = sentenceEnders.split(i)#sentenceEnders.split(i) i.split(".")
		for j in sentenceList:
			if(not(j.isspace())):
				pr.write(j)
				pr.write('\n')
		
		
		
		#sentenceList = sentenceEnders.split(i)#sentenceEnders.split(i) i.split(".")
	#for j in sentenceList:
