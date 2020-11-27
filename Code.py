#Ngin Baghbanzade
#810196599
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import sys
import time
import random
start_time = time.time()
np.set_printoptions(threshold=sys.maxsize)
from random import randrange

####################################################
#df = pd.read_csv("persian.csv")
file = open("persian.txt","r")
lines = file.read()
lines = lines.split()
#ignore = np.array(df['id'])
ignore = np.array(lines)
data = pd.read_csv("train_test.csv")
eData = pd.read_csv("evaluate.csv")
label = np.array(data['label'])
text = np.array(data['text'])
eId = np.array(eData['id'])
eText = np.array(eData['text'])
line = int(len(label)*0.8)

splitted = []
counter = 0
for i in range(0, line):
	s = text[i].split()
	splitted.append([s, counter])
	counter += 1

word = []
poet = []
for i in range(0, len(splitted)):
	for j in range(0, len(splitted[i][0])):
		word.append(splitted[i][0][j])
		poet.append(splitted[i][1])
hafezSum = 0
sadiSum = 0
for i in range(0, len(word)):
	if(label[poet[i]] == 'hafez'):
		hafezSum += 1
	else:
		sadiSum += 1

toAppend = np.array([])
frequencyTable = np.array([])
word = np.array(word)
for i in range(0, len(word)):
	where = np.argwhere(frequencyTable==word[i])
	if(len(where) == 0):
		if(label[poet[i]] == 'hafez'):
			toAppend = np.array([word[i], 1, 0, 1/hafezSum, 0])
			frequencyTable = np.concatenate((frequencyTable, toAppend))
		else:
			toAppend = np.array([word[i], 0, 1, 0, 1/sadiSum])
			frequencyTable = np.concatenate((frequencyTable, toAppend))
	else:
		if(label[poet[i]] == 'hafez'):
			frequencyTable[where+1] = int(frequencyTable[where+1]) + 1
			frequencyTable[where+3] = int(frequencyTable[where+1])/hafezSum
		else:
			frequencyTable[where+2] = int(frequencyTable[where+2]) + 1
			frequencyTable[where+4] = int(frequencyTable[where+2])/sadiSum
hafez = hafezSum/hafezSum+sadiSum
sadi = sadiSum/hafezSum+sadiSum

pHafez = 1
pSadi = 1

correctDetectedHafezes = 0
correctDetectedSadis = 0
detectedHafezes = 0
detectedSadis = 0
correctDetectes = 0
numOfHafez = 0
numOfSadi = 0
# outId = []
# outPoet = []
# for j in range(0, len(eText)):
# 	pHafez = 1
# 	pSadi = 1
# 	flag = False
# 	W1 = ""
# 	W2 = eId[j]
# 	for i in range(0, len(text[j].split())):
# 		where = np.argwhere(frequencyTable==text[j].split()[i])
# 		if(True):
# 			if(len(where) != 0):
# 				flag = True
# 				if(float(frequencyTable[where+3]) != 0):
# 					pHafez *= float(frequencyTable[where+3])
# 				elif(float(frequencyTable[where+3]) == 0):
# 					pHafez *= 1/(hafezSum+2)
# 				if(float(frequencyTable[where+4]) != 0):
# 					pSadi *= float(frequencyTable[where+4])
# 				elif(float(frequencyTable[where+4]) == 0):
# 					pSadi *= 1/(sadiSum+2)
#
# 	if(flag):
# 		pHafez *= hafez
# 		pSadi *= sadi
# 		if(pSadi > pHafez):
# 			W1 = 'saadi'
# 			#print("Saadi", '\t', label[j])
# 			detectedSadis = detectedSadis + 1
# 			if(label[j] == 'saadi'):
# 				numOfSadi = numOfSadi + 1
# 				correctDetectedSadis = correctDetectedSadis + 1
# 			else:
# 				numOfHafez = numOfHafez + 1
# 		elif(pHafez > pSadi):
# 			W1 = 'hafez'
# 			#print("Hafez", '\t', label[j])
# 			detectedHafezes = detectedHafezes + 1
# 			if(label[j] == 'hafez'):
# 				numOfHafez = numOfHafez + 1
# 				correctDetectedHafezes = correctDetectedHafezes + 1
# 			else:
# 				numOfSadi = numOfSadi + 1
# 		else:
# 			rand = random.uniform(40, 1)
# 			if(int(rand)%2 == 0):
# 				numOfSadi = numOfSadi + 1
# 				if(label[j] == 'saadi'):
# 					print("Saadi", '\t', label[j])
# 					correctDetectedSadis = correctDetectedSadis + 1
# 			else:
# 				#print("Hafez", '\t', label[j])
# 				numOfHafez = numOfHafez + 1
# 				if(label[j] == 'hafez'):
# 					correctDetectedHafezes = correctDetectedHafezes + 1
# 	else:
# 		rand = random.uniform(40, 1)
# 		if(int(rand)%2 == 0):
# 			W1 = 'saadi'
# 			numOfSadi = numOfSadi + 1
# 			if(label[j] == 'saadi'):
# 				#print("Saadi", '\t', label[j])
# 				correctDetectedSadis = correctDetectedSadis + 1
# 		else:
# 			W1 = 'hafez'
# 			#print("Hafez", '\t', label[j])
# 			numOfHafez = numOfHafez + 1
# 			if(label[j] == 'hafez'):
# 				correctDetectedHafezes = correctDetectedHafezes + 1
# 	outId.append(W2)
# 	outPoet.append(W1)
# df = {'id': outId, 'poet': outPoet}
# df = pd.DataFrame(df)
# df.to_csv('output.csv', header=False, index=False)

for j in range(line+1, len(text)):
	pHafez = 1
	pSadi = 1
	flag = False
	for i in range(0, len(text[j].split())):
		where = np.argwhere(frequencyTable==text[j].split()[i])
		if(True):
			if(len(where) != 0):
				flag = True
				if(float(frequencyTable[where+3]) != 0):
					pHafez *= float(frequencyTable[where+3])
				elif(float(frequencyTable[where+3]) == 0):
					pHafez *= 1/(hafezSum+2)
				if(float(frequencyTable[where+4]) != 0):
					pSadi *= float(frequencyTable[where+4])
				elif(float(frequencyTable[where+4]) == 0):
					pSadi *= 1/(sadiSum+2)

	if(flag):
		pHafez *= hafez
		pSadi *= sadi
		if(pSadi > pHafez):
			#print("Saadi", '\t', label[j])
			detectedSadis = detectedSadis + 1
			if(label[j] == 'saadi'):
				numOfSadi = numOfSadi + 1
				correctDetectedSadis = correctDetectedSadis + 1
			else:
				numOfHafez = numOfHafez + 1
		elif(pHafez > pSadi):
			#print("Hafez", '\t', label[j])
			detectedHafezes = detectedHafezes + 1
			if(label[j] == 'hafez'):
				numOfHafez = numOfHafez + 1
				correctDetectedHafezes = correctDetectedHafezes + 1
			else:
				numOfSadi = numOfSadi + 1
		else:
			rand = random.uniform(40, 1)
			if(int(rand)%2 == 0):
				numOfSadi = numOfSadi + 1
				if(label[j] == 'saadi'):
					#print("Saadi", '\t', label[j])
					correctDetectedSadis = correctDetectedSadis + 1
			else:
				#print("Hafez", '\t', label[j])
				numOfHafez = numOfHafez + 1
				if(label[j] == 'hafez'):
					correctDetectedHafezes = correctDetectedHafezes + 1
	else:
		rand = random.uniform(40, 1)
		if(int(rand)%2 == 0):
			numOfSadi = numOfSadi + 1
			if(label[j] == 'saadi'):
				#print("Saadi", '\t', label[j])
				correctDetectedSadis = correctDetectedSadis + 1
		else:
			#print("Hafez", '\t', label[j])
			numOfHafez = numOfHafez + 1
			if(label[j] == 'hafez'):
				correctDetectedHafezes = correctDetectedHafezes + 1

correctDetectes = correctDetectedHafezes + correctDetectedSadis
print("Recall: ", correctDetectedHafezes/numOfHafez)
print("Presicion: ", correctDetectedHafezes/detectedHafezes)
print("Accuracy: ", correctDetectes/(numOfHafez+numOfSadi))
print("--- %s seconds ---" % (time.time() - start_time))
