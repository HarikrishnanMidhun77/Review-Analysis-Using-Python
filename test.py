import glob
import os
path1='/home/harikrishnan-midhun/Desktop/MainPro/sub_aspects/'
print glob.glob(os.path.join(path1+'camera/', ''))

subAspects=['batery','camera','display','performance','price','sound']
for i in subAspects:
	for filename in glob.glob(os.path.join(path1+i+'/', '')):
			print filename
for i in subAspects:			
	for filename in os.listdir(path1+i):
		print filename
a="lfkjkdfjbnkdfjbn"
c="6654564654"
print a+c
