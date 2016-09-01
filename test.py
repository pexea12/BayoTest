import random
import shutil
import os

def createTestCases(n=5, seed=None):
	'''
	Create test cases for the sort function
	1. Generate a sorted array
	2. Shuffle the array to get a new array
	3. Sort the new array
	4. Compare the array in (3) and the array in (1)
		If they are the same, test case is passed
	
	Params:
		n: number of test cases
		seed: the seed for random
	'''
		
	# Delete folder 'solution' and 'test'
	shutil.rmtree('solution')
	shutil.rmtree('test')
	
	os.makedirs('solution')
	os.makedirs('test')
		
	# Set random seed
	random.seed(seed)
	
	for i in range(n):
		print('Generate test case %d' % i)
		
		# Generate random array
		array = random.sample(range(-2**31, 2**31 - 1), int(1e6))
		
		# Write random array to input file	
		testFile = open('test/%d.txt' % i,'w')
		
		for num in array:
			testFile.write('%d\n' % num)
			
		testFile.close()
		
		# Sort random array
		array.sort()
		
		# Write random array to output file
		solutionFile = open('solution/%d.txt' % i, 'w')
		
		for num in array:
			solutionFile.write('%d\n' % num)
			
		solutionFile.close()

from sort import sort

def testSortFunction(sortFunc=sort, verbose=True):
	'''
	Test the sort function
	
	Params:
		sortFunc (default is the sort function in sort.py)
		verbose (default True): print log message
	'''
	
	# Delete all files in folder 'sort', 'test' and 'solution'
	shutil.rmtree('sort')
	
	os.makedirs('sort')
	
	# List all the file in test folder
	testFiles = os.listdir('test')
	solutionFiles = os.listdir('solution')
	
	for testFile in testFiles:
		# Use sort function
		sortFunc(fileIn='test/' + testFile, fileOut='sort/' + testFile, verbose=verbose) 
		
	# Compare file in folder 'sort' and folder 'solution'
	import filecmp
	
	count = 0
	for solution in solutionFiles:
		if filecmp.cmp('solution/' + solution, 'sort/' + solution, shallow=False):
			print('Compare file %s: Passed' % solution)
			count += 1		
		else:
			print('Compare file %s: Failed' % solution)
	
	print('Result: %d/%d' % (count, len(solutionFiles)))

	
if __name__ == '__main__':
	select = input('Do you want to generate test cases or not? (y/n) ')
	
	if select == 'y' or select == 'Y':
		print('Generate 5 test cases')
		createTestCases(n=5)
	
	testSortFunction()
