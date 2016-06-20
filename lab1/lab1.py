# coding: utf-8

"""
ELECTRE method

Subject Area:

* Choose of a corporate regional manager for new openning position in office *
* In Andalousia [Spain] with staff consisting of french and spanish employees *


Table of critarias:
---------------------------------------------------------------------------------------------
|	Criteria			Scale				Value [1-3]		Tendency[Min-Max]	Weight[1-5] |
|-------------------------------------------------------------------------------------------|
|						High					= 3											|
| Salary				Middle					= 2				MIN 				3		|
|						Low						= 1 										|
|-------------------------------------------------------------------------------------------|
|						Large					= 3											|
| Expirience			Middle					= 2				MAX 				4		|
|						Low						= 1											|
|-------------------------------------------------------------------------------------------|
|						Single					= 1											|
| Family/Mobility		Married					= 2				MIN					2		|
|						Married with children	= 3 										|
|-------------------------------------------------------------------------------------------|
|						English+Spanish+French	= 4											|
| Languages				English+Spanish			= 3				MAX 				5		|
|						English+French			= 2											|
|						English					= 1											|
---------------------------------------------------------------------------------------------

"""


class Electre():
	"""realisation of ELECTRE algorithm"""
	import numpy as NUM

	def __init__(self, weight):
		self.weight = weight
		self.m = len(weight)
		self.n = 0
		self.result = []
		self.alternatives = []
		self.meaning = []

	def fillMatrix(self):
		for i in range(int(self.n)):
			self.result.append([])
			for j in range(int(self.n)):
				self.result[i].append(int(0))


	def countValue(self, index, value1, value2):

		if int(value1) == int(value2):
			return 0

		if (self.meaning[index] is "max") and (int(value1) > int(value2)):
			return 1;

		if (self.meaning[index] is "max") and (int(value1) < int(value2)):
			return 0;

		if (self.meaning[index] is "min") and (int(value1) < int(value2)):
			return 1;

		if (self.meaning[index] is "min") and (int(value1) > int(value2)):
			return 0;

	def getValue(self, i, j):
		value1 = self.alternatives[i]
		value2 = self.alternatives[j]
		# POSITIVE
		calcs = ""
		val1 = 0
		key = 0
		calcs = ""
		for k in range(self.m):
			key = self.countValue(k,value1[k],value2[k])
			val1 += int(value1[k])*int(key)

		# NEGATIVE
		calcs = ""
		val2 = 0
		key = 0
		calcs = ""
		for k in range(self.m):
			key = self.countValue(k,value2[k],value1[k])
			val2 = int(value2[k])*int(key)

		if (int(val1) != 0) and (int(val2) != 0):
			return float(val1)/float(val2)

		else:
			return 0.0

		

	def method(self, table, sign):

		self.n = self.NUM.shape(table)[0] # number of alternatives		
		self.alternatives = table
		self.meaning = sign


		if int(self.m) != int(self.NUM.shape(table)[1]): 
			raise IndexError("mismatch of weight and criteria number!")

		self.fillMatrix()

		for i in range(self.n):
			for j in range(self.n):
				if (int(i) != int(j)):
					value = float(self.getValue(i,j))
					if (float(value) >= 1.0):
						self.result[i][j] = float(value)
					elif (float(value) != 0):
						self.result[j][i] = float(1.0/float(value))

		#print("all right!")

	def printMatrix(self):
		print("Preference Matrix")
		print
		for line in self.result:
			str = ""
			for i in range(self.n):
				str += "%.2f" % line[i] + '  '
			print(str + '\n')

	def printGraph(self, threshold):
		print("Preference Graph")
		for i in range(self.n):
			for j in range(self.n):
				if(float(self.result[i][j]) >= float(threshold)):
					print(str(i) + ' -> ' + str(j))





"""
Alternatives for openning possitions and there characteristics from HR department

0 - Salary		[1-3:Min]   
1 - Expirience	[1-3:Max]   
2 - Mobility	[1-3:Min]
3 - Languages 	[1-4:Max]
"""
# Names after index number to interprite the result
coding = [
		{"0": "Michael Scott"},
		{"1": "James Helbert"},
		{"2": "Dwight Shroote"},
		{"3": "Andrew Bernard"},
		{"4": "Pamela Beasly"},
		{"5": "Ryan Howard"},	
]

alternatives = [
				[3,3,2,2],
				[2,2,3,3],
				[2,3,2,3],
				[3,3,1,1],
				[2,1,3,4],
				[1,2,1,3],
] # Information about participants, filled as algorithm ELECTRA required

weight = [3,4,2,5] # Weight of each position
meaning = ["min","max","min","max"] # Wieght function gor choosing

electra = Electre(weight)
electra.method(alternatives,meaning)
electra.printMatrix()
electra.printGraph(1.25)
print('Decode numbers with names')
for line in coding:
	print line
