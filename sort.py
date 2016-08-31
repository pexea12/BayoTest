import numpy as np

def sort(filename='input.txt'):
	'''
	Sort all the signed 32-bit integers in file filename
	Return a numpy array which contains all the sorted signed 32-bit integers
	'''
	
	array = np.loadtxt(filename, delimiter='/n', dtype=np.int32)
	array.sort()
	
	return array
