# BayoTest

For the Github repository, please visit: https://github.com/pexea12/BayoTest

### **Dependencies**
This project is built by **Python 3.5**, using **Numpy**. Numpy is a very strong library which supports scientific computing. 
Run `python sort.py` to see the result. View `sort.py` to see the implementation of the sort function.  
Run `python test.py` to see the test.  

### **Input format** (*input.txt*)
The first line contains the total numbers.  
After the first line, each line contain a number. For example:

> 4
> 1  
> 5  
> 7  
> 4  

which means the data is [1, 5, 7, 4].
In *input.txt*, there are 1 million lines + 1 first line. Each line contains an integer.

### **Output format** (*output.txt*)
The first line contains the total numbers.  
After the first line, each line contains a number after sorting. For example:

> 4
> 1  
> 4  
> 5  
> 7  

which means the sorted data is [1, 4, 5, 7].
In *output.txt*, there are 1 million lines + 1 first line. Each line contains an integer.

### **generateSample.py**
If running directly `python generateSample.py`, the program will generate data and write them to file.

 1. `generateData(n=int(1e6), seed=None)`
	* Generate n random signed 32-bit integers (from -2^31 to 2^31 - 1)
	* ***Params:***
	**n**: number of random integers (*default 1e6*)
	**seed**: the seed of random (*default = None (use system time)*)
	* ***Return:***
	A numpy array which contains n random integers
 2. `writeDataToFile(array, filename='input.txt')`
	* Write n random signed 32-bit integers to file filename
	* ***Params***:
	  **array: ** array to write to the file
	  **filename: ** name of the file
    
### **sort.py**	
If running directly `python sort.py`, the program will execute `sort()`

`sort()` will attempt to divide the file into 4 chunks, each chunk contains 250 thousand numbers.  
Because the total size of 250 thousand numbers is only 1 million bytes (< 3MB), we can load each file into the memory, sort the numbers and write them to the other files.
After that, all we need to do is merge these files into one by using the simple merging algorithm which is the same as the algorithm using in Merge Sort.  

In fact, the total memory using by `sort()` is about 2.4MB.  

 1. `sort(fileIn='input.txt', fileOut='output.txt', verbose=False)`
	* Sort all the signed 32-bit integers in file filename
	* ***Params***:
		**fileIn**: contains unsorted array (*default input.txt*)
		**fileOut**: contains sorted array (*default output.txt*)

### **test.py**	
If running directly python `test.py`, the program will execute `createTestCases(n=5)` and then `testSortFunction()`

 1. `createTestCases(n=5, seed=None)`
	* Create test cases for the sort function
	1. Generate a random array
	2. Write the random array to folder test
	3. Sort the random array and write it to folder solution
	We will compare the sorted array after using sort() in sort.py and the array in (3)
		If they are the same, test case is passed
	* ***Params***:
		**n**: number of test cases
		**seed**: the seed for random 

 2. `testSortFunction(sortFunc=sort, verbose=True)`
	* Test the sort function
	* ***Params***:
		**sortFunc** (*default is the sort function in sort.py*)
		**verbose** (*default True*): print log message 


### Folder

**test**: Contain the input data for test  
**solution**: Contain the correct output data for each test  
**sort**: Contain the output data which are generated by function sort  

