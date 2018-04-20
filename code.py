# Mike Quaid 19042018

import numpy # numpy is a package or library of functions

data=numpy.genfromtxt('iris.txt',delimiter=',') # read data file into an array

# each element of the array is seperated by a comma in the raw data file
# the first column is [:,0]
# the first row is [0]

# calculate the mean of each column in the array
meansepallength=numpy.mean(data[:,0]) 
print(meansepallength)

meansepalwidth=numpy.mean(data[:,1]) 
print(meansepalwidth)

meanpetallength=numpy.mean(data[:,2]) 
print(meanpetallength)

meanpetalwidth=numpy.mean(data[:,3]) 
print(meanpetalwidth)

# calculate the maximum value in each column in the array
maxsepallength=numpy.max(data[:,0])
print(maxsepallength)

maxsepalwidth=numpy.max(data[:,1])
print(maxsepalwidth)

maxpetallength=numpy.max(data[:,2])
print(maxpetallength)

maxpetalwidth=numpy.max(data[:,3])
print(maxpetalwidth)
