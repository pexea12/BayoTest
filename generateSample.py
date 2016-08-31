import random
import numpy as np

def generateData(n=int(1e6), seed=None):
	'''
	Generate n random signed 32-bit integers (from -2^31 to 2^31 - 1)
	Params:
		n: number of random integers (default = 1e6)
		seed: the seed of random (default = None (use system time))
	Return:
		A numpy array which contains n random integers
	'''
	# Set the seed of random
	np.random.seed(seed)
	
	return np.random.randint(-2**31, 2**31 - 1, size=n)

	
def writeDataToFile(filename='input.txt', n=int(1e6), seed=None):
	'''	
	Write n random signed 32-bit integers to file filename
	'''
	array = generateData(n=n, seed=seed)
	
	np.savetxt(filename, array, delimiter='\n', fmt='%d')
	
	
	
	
	
	
