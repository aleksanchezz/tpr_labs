# coding: utf-8
from operator import add
from random import randint
import random

class Specie:


	def __init__(self, tabl, n):
		self.firstPop = 0
		self.result = 0
		self.gene = []
		self.n = n
		self.values = tabl
		self.matrix = []
		for i in range(int(self.n)):
			self.matrix.append([])
			for j in range(int(self.n)):
				self.matrix[i].append(int(0))


	"""
	Finctions to deifne|fill in|create assignment matrix and gene
	"""
	def buildPopulation(self):
		"""
		Randomly fill first assignment matrix
		"""
		count = 0
		while(not self.checkMatrix()):
			self.emptyMatrix()
			count += 1
			for i in range(self.n):
				index = randint(0,4)
				self.matrix[i][index] = int(1)
		return count


	def getGeneFromMatrix(self):
		for i in range(self.n):
			self.gene.append(0)
		i = -1
		for line in self.matrix:
			i += 1
			self.gene[i] = line.index(1)


	def fillMatrixFromGene(self, gene):
		self.gene = gene
		for i in range(self.n):
			self.matrix[i][self.gene[i]] = int(1)

	def fillMatrixWithotGene(self):
		self.firstPop = self.buildPopulation()
		self.getGeneFromMatrix()

	"""
	Extra functions to assisting in filling in the assignment matrix
	"""
	def emptyMatrix(self):
		for i in range(int(self.n)):
			for j in range(int(self.n)):
				self.matrix[i][j] = int(0)


	def checkMatrix(self):
		"""
		Check that created assignation matrix fit the requirements 
		"""
		# Check that sum of each row equals 1
		for line in self.matrix:
			for i in range(self.n):
				if(sum(line) != 1):
					return False
		# Check that sum of each colomn equals 1
		line = self.matrix[0]
		for i in range(1,self.n):
			line =  map(add,line,self.matrix[i])
		for p in line:
			if p != 1:
				return False

		return True


	def calculateValue(self):
		calc = 0
		for i in range(self.n):
			for j in range(self.n):
				calc += int(self.matrix[i][j])*int(self.values[i][j])
		return calc

	"""
	Print matrix block
	"""
	def printMatrix(self):
		print("Assignment Matrix")
		for line in self.matrix:
			st = ""
			for i in range(self.n):
				st += str(line[i]) + ' '
			print(st)


	def printValues(self):
		print("Values Matrix")
		for line in self.values:
			st = ""
			for i in range(self.n):
				st += str(line[i]) + ' '
			print(st)

	"""
	GET functions
	"""
	def getGene(self):
		return self.gene

	def getMatrix(self):
		return self.matrix

	def getCalculation(self):
		self.result = self.calculateValue()

class Experiment:

	def __init__(self, capacity, n):
		self.n = n
		self.capacity = capacity
		self.genes = []
		self.species = []
		self.newgenes = []

	def generateGene(self):
		basis = [x for x in range(self.n)]
		random.shuffle(basis)
		return basis
            

	def generateGenes(self):
		for i in range(self.capacity):
			self.genes.append(self.generateGene())
			# print self.genes[i]

	def createSpecies(self, tabl):
		for i in range(self.capacity):
			spc = Specie(tabl,self.n)
			spc.fillMatrixFromGene(self.genes[i])
			spc.getCalculation()
			self.species.append(spc)

	def printGenes(self):
		print("$$$$$$$$$$$$$$$$$$")
		i = 0
		for line in self.newgenes:
			i += 1
			print i, ' ',line

	def iteration(self):

		self.newgenes = list(self.genes)
		
		self.crossing()
		# self.printGenes()

		self.mutating()
		# self.printGenes()

		self.genes = list(self.newgenes)


	def crossTwoGenes(self, gene1, gene2):
		res = []
		res.append([gene1[i] for i in [0, 1, 2]] + [gene2[i] for i in [3, 4]])
		res.append([gene2[i] for i in [0, 1, 2]] + [gene1[i] for i in [3, 4]])
		return res

	def mutateTwoGenes(self, gene1, gene2):
		res = []

		element = gene1[2]
		gene1[2] = gene1[3]
		gene1[3] = element

		element = gene2[2]
		gene2[2] = gene2[3]
		gene2[3] = element
		
		res.append(gene1)
		res.append(gene2)

		# res.append(gene1[::-1])
		# res.append(gene2[::-1])


		return res

	def crossing(self):
		for i in range(self.capacity-1):
			buff = []
			buff = self.crossTwoGenes(self.newgenes[i],self.newgenes[i+1])
			self.newgenes[i] = buff[0]
			self.newgenes[i+1] = buff[1]

	def mutating(self):
		for i in range(self.capacity-1):
			buff = []
			buff = self.mutateTwoGenes(self.newgenes[i],self.newgenes[i+1])
			self.newgenes[i] = buff[0]
			self.newgenes[i+1] = buff[1]

	def getValues(self):
		mininim = self.species[0].result
		min_index = 0
		print"########################"
		l = len(self.species)
		for i in range(self.capacity):
			st = ""
			m = l / self.capacity
			for j in range(m):
				index = i + j*self.capacity
				if self.species[index].result < mininim:
					mininim = self.species[index].result
					min_index = index
				st += str(self.species[index].result) + ' -> '
				#st += str(i + j*self.capacity) + ' -> '
			print st
		return min_index

	def getResultValue(self, index):
		return self.species[index].result

	def getResultMatrix(self, index):
		print
		self.species[index].printMatrix()
		print "Best found gene"
		return self.species[index].getGene()