#parsing comments
import re
# import pandas as pd

# fullCorpus = pd.DataFrame({
	# 'label' : labelList,
	# 'text' : textList})
	
with open("comments.csv","r") as f:
	words = []
	digits=[]
	

	for line in f:
		# comment.append(split(line))
		words.append(re.findall('\w*',line))
		digits.append(re.findall('\d*',line))
		
		#findall() looks for match directly
		#split() looks for words separated by some match
		#regexes are used for tokenizing: W is for words, S is for whitespaces
		#lowercase looks for a TRUE on the match, uppercase looks for a FALSE on the match
		
		# re.split('\W+',line) #looks for splits and gets words
		# re.findall('\S+', line) #looks for non-blank spaces
		# re.findall('\w+', line) #looks for non-blank spaces
		
# ints = [str(i) for i in range(10)]
# units = ['oz',' oz']	
# for c in line2:
	# if c in ints:
		# print('works')
	# def split(string):
		# return [char for char in string]		
