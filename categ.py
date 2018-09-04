#fp = open('/home/harikrishnan-midhun/Desktop/MainPro/keywords/battery.txt', 'r')  
rootpath='/home/harikrishnan-midhun/Desktop/MainPro/'
sndfl=open(rootpath+'sound.txt', 'w') 
camfl=open(rootpath+'camera.txt', 'w') 
batfl=open(rootpath+'batery.txt', 'w') 
disfl=open(rootpath+'display.txt', 'w') 
perfl=open(rootpath+'performance.txt', 'w') 
prifl=open(rootpath+'price.txt', 'w') 
c=0;
def lsmake(path):
	abls=[]
	with open(path) as fp:  
   		line = fp.readline()
	  	while line:
	       #print("Line {}: {}".format(cnt, line.strip()))
	       		if(not(line.isspace())):
	       			abls.append(line.strip());
	       		line = fp.readline()
	return abls
	     
filepathtest = '/home/harikrishnan-midhun/Desktop/MainPro/phone_reviews.txt'   #Testset.txt  phone_reviews.txt'  
with open(filepathtest) as fp2:  
	line = fp2.readline()
	#line=line.decode('utf-8')
	
	
	while line:	
		if(not(line.isspace())):
			for i in lsmake(rootpath+'keywords/sound.txt'  ):
				if(i in line):
					sndfl.write(line);
		for i in lsmake(rootpath+'keywords/camera.txt'  ):
				if(i in line):
					camfl.write(line);
		for i in lsmake(rootpath+'keywords/battery.txt'  ):
				if(i in line):
					batfl.write(line);
		for i in lsmake(rootpath+'keywords/display.txt'  ):
				if(i in line):
					disfl.write(line);
		for i in lsmake(rootpath+'keywords/performance.txt'  ):
				if(i in line):
					perfl.write(line);
		for i in lsmake(rootpath+'keywords/price.txt'  ):
				if(i in line):
					prifl.write(line);
       				
		line = fp2.readline()

