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

	
def writeDataToFile(array, filename='input.txt'):
	'''	
	Write array to file filename
	'''
	np.savetxt(filename, array, fmt='%d', delimiter='\n', header=str(len(array)), comments='')

if __name__ == '__main__':
	array = generateData()
	
	writeDataToFile(array)	
	
	
	
	
