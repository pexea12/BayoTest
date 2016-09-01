import numpy as np
import time

def sort(fileIn='input.txt', fileOut='output.txt', verbose=False):
	'''
	Sort all the signed 32-bit integers in file filename
	Return a numpy array which contains all the sorted signed 32-bit integers
	Params:
		fileIn: contains unsorted array (default input.txt)
		fileOut: contains sorted array (default output.txt)
		verbose: (default False)
			if verbose is True, log message will be print
			 (log message about time)
			 
	Return:
		sorted array
	'''
	
	# Load array from fileIn
	if verbose:
		print('\n\tLoading array from %s...' % fileIn)
	
	# Time before loading 	
	loadTimeStart = time.time()
	
	array = np.loadtxt(fileIn, delimiter='/n', dtype=np.int32)
	
	# Time after loading
	loadTimeStop = time.time()
	
	if verbose:
		print('\tLoad time: %.6f' % (loadTimeStop - loadTimeStart))
		
	# Sort array
	if verbose:
		print('\tSorting array...')
	
	# Time before sorting
	sortTimeStart = time.time()
	
	array.sort()
	
	# Time after sorting
	sortTimeStop = time.time()
	
	if verbose:
		print('\tSort time: %.6f' % (sortTimeStop - sortTimeStop))
		
	# Save sorted array to fileOut
	if verbose:
		print('\tSaving sorted array to %s' % fileOut)
	
	# Time before saving
	saveTimeStart = time.time()
	
	np.savetxt(fileOut, array, delimiter='/', fmt='%d')
	
	# Time after saving
	saveTimeStop = time.time()
	
	if verbose:
		print('\tSave time: %.6f' % (saveTimeStop - saveTimeStart))
	
	return array
	
	
if __name__ == '__main__':
	# Generate data
	print('Generating data...')
	from generateSample import writeDataToFile
	writeDataToFile()

	# Sort array and write to file
	print('Sorting...')
	sort(verbose=True)
