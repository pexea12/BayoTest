import numpy as np
from generateSample import writeDataToFile
import os

def readNum(f, type=int):
	return type(f.readline().rstrip())


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
	
	array = np.array([], dtype=np.int32)
	totalFiles = 0
	
	# Divide file into chunks. Read only 250k numbers at one time 
	margin = 250000

	print('Dividing the file into chunks...')	
	with open(fileIn, 'r') as fileInput:
		n = readNum(fileInput)
		
		for i in range(n):
			num = readNum(fileInput)
			array = np.append(array, num)	
			
			if (i + 1) % margin == 0 or i + 1 == n:
				# Sort array
				array.sort()
		
				# Save the chunk to a file
				fileName = '0' + str(totalFiles)
				print('Chunk %d' % totalFiles)
				
				totalFiles += 1
				writeDataToFile(array, filename=fileName)
		
				# Empty the array
				array = np.array([], dtype=np.int32)
	
	
	# Merge the sort arrays
	print('Merging...')
	stage = 0
	
	while totalFiles > 1:
		i = 0
		count = 0
		
		while i < totalFiles:
			# open temporary file to merge
			f1 = open(str(stage) + str(i), 'r')
			f2 = open(str(stage) + str(i + 1), 'r')
			
			with open(str(stage + 1) + str(count), 'w') as f:
				n1 = readNum(f1)
				n2 = readNum(f2)
				
				j1 = 0
				j2 = 0
				
				f.write('%d\n' % (n1 + n2))
				
				num1 = readNum(f1)
				num2 = readNum(f2)
			
				while (j1 < n1 and j2 < n2):
					try:
						if num1 < num2:
							f.write('%d\n' % num1)
							j1 += 1
							num1 = readNum(f1)
						else:
							f.write('%d\n' % num2)
							j2 += 1		
							num2 = readNum(f2)
					except ValueError:
						break
												
				while (j1 < n1):
					try:
						f.write('%d\n' % num1)
						j1 += 1
						num1 = readNum(f1)
					except ValueError:
						break
					
				while (j2 < n2):
					try:
						f.write('%d\n' % num2)
						j2 += 1
						num2 = readNum(f2)
					except ValueError:
						break
							
			f1.close()
			f2.close()
			
			# Remove these two files
			os.remove(str(stage) + str(i))
			os.remove(str(stage) + str(i + 1))
			
			count += 1
			i += 2
		
		stage += 1
		totalFiles = count
	
	os.rename(str(stage) + '0', fileOut)
	
	print('Done!')
	
if __name__ == '__main__':
	sort()
	
