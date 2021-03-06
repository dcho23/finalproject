import csv 
import random
import sys
import pprint as pp

filename=sys.argv[1]
wordDict={}
catList=[]

for line in open(filename,'r'):
	if 'Category' not in line:
		wordDict[line.split(';')[0]]=line.split(';')[1].strip('\n')
	else:
		catList.append(line.split(';'))
betterCat=[]
for splitline in catList:
	betterCat.append(splitline[1].strip('\n'))

def finalFunc(lb,ub):
	for i,line in enumerate(open(filename,'r')):
		if i in range(lb,ub):
			print(line.split(';')[0])

for i in betterCat:
	print(i)

iList=[]
bList=[]
cList=[]

cat_selection=input("Which category would you like to select? ")

if cat_selection in betterCat[0:len(betterCat)-1]:
	for i,cat in enumerate(betterCat):
		if cat_selection in cat:
			iList.append(i)
			iList.append(i+1)
	for i,dog in enumerate(open(filename,'r')):
		if betterCat[iList[0]] in dog:
			bList.append(i)
		if betterCat[iList[1]] in dog:
			bList.append(i)
	finalFunc(bList[0],bList[1])
	
	selection=input("Please enter your selection here: ").lower()
	if selection in wordDict.keys():
		answer=input("What is the correct answer? ").lower()
		if answer == wordDict[selection]:
			print("Correct!")
		else:
			print("Sorry, answer is: ",wordDict[selection])
	else:
		print("Sorry, that word isn't stored. Please try again.")

elif cat_selection in betterCat:
	for i,line in enumerate(open(filename,'r')):
		cList.append(i)
		if cat_selection in line:
			iList.append(i)
	iList.append(cList[len(cList)-1])
	finalFunc(iList[0],iList[1])
	
	selection=input("Please enter your selection here: ").lower()
	if selection in wordDict.keys():
		answer=input("What is the correct answer? ").lower()
		if answer == wordDict[selection]:
			print("Correct!")
		else:
			print("Sorry, answer is: ",wordDict[selection])
	else:
		print("Sorry, that word isn't stored. Please try again.")

else:
	print("Sorry, that category isn't stored. Please try again.")