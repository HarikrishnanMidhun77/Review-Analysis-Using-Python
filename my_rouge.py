from rouge import Rouge 
import sys
reload(sys)
sys.setdefaultencoding('utf8')
path='/home/harikrishnan-midhun/Desktop/MainPro/'
path2='/home/harikrishnan-midhun/Desktop/MainPro/AspectLevelSumm/'

def find_rouge(file1,file2):
	with open(file1, 'r') as myfile:
		text1=myfile.read()
	with open(file2, 'r') as myfile:
		text2=myfile.read()
	rouge = Rouge()
	scores = rouge.get_scores(text1, text2)
	print scores
	return scores

find_rouge(path+'camera_human.txt',path2+'camera')