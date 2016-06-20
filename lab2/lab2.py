# coding: utf-8
import numpy as NUM
from genetic import Specie, Experiment

matrix = [
		[1, 4, 7, 9, 4],
		[9, 3, 8, 7, 4],
		[3, 4, 6, 8, 2],
		[8, 9, 4, 2, 7],
		[7, 6, 2, 8, 5],
		]

n = NUM.shape(matrix)[0]
m = NUM.shape(matrix)[1]

if int(n) == int(m):

	# Create zero population
	exper = Experiment(10,n)
	exper.generateGenes()
	exper.createSpecies(matrix)

	# Start actions
	iterations = 20
	for i in range(iterations):
		exper.iteration()
		exper.createSpecies(matrix)

	minim = exper.getValues()

	print "Calculated via GA values for Assignment Problem [iterations={iters}]".format(iters=iterations)
	print "Minimal found value = {val}".format(val=exper.getResultValue(minim))
	print "Iteration = {val}".format(val=minim/n)
	print exper.getResultMatrix(minim)

else:
	print("matrix is not quadric!")