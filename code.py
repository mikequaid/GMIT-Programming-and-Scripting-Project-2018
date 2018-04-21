# Mike Quaid 19042018
# Below is the python scripts analysing the Iris dat-set
# Note 1 - Where appropriate numbers are rounded to 2 decimal places
#          for presentation purposes via built-in function round()
#          https://docs.python.org/3/library/functions.html#round

import numpy # numpy is a package or library of functions

data=numpy.genfromtxt('iris.txt',delimiter=',') # read data file into an array

# each element of the array is seperated by a comma in the raw data file
# the first column is [:,0]
# the first row is [0]

# calculate the mean of each column in the array
meansepallength=numpy.mean(data[:,0]).round(2)
print('mean sepal length is',meansepallength)

meansepalwidth=numpy.mean(data[:,1]).round(2)
print('mean sepal width is',meansepalwidth)

meanpetallength=numpy.mean(data[:,2]).round(2)
print('mean petal length is',meanpetallength)

meanpetalwidth=numpy.mean(data[:,3]).round(2)
print('mean sepal length is',meanpetalwidth)

# calculate the maximum value in each column in the array
maxsepallength=numpy.max(data[:,0])
print('max sepal length is',maxsepallength)

maxsepalwidth=numpy.max(data[:,1])
print('max sepal width is',maxsepalwidth)

maxpetallength=numpy.max(data[:,2])
print('max petal length is',maxpetallength)

maxpetalwidth=numpy.max(data[:,3])
print('max petal length is',maxpetalwidth)

# calculate the minimum value in each column in the array
minsepallength=numpy.min(data[:,0])
print('min sepal length is',minsepallength)

minsepalwidth=numpy.min(data[:,1])
print('min sepal width is',minsepalwidth)

minpetallength=numpy.min(data[:,2])
print('min petal length is',minpetallength)

minpetalwidth=numpy.min(data[:,3])
print('min petal width is',minpetalwidth)

# calculate the percentile value in each column in the array
persepallength=numpy.percentile(data[:,0],.8)
print('80th Percentile sepal length is',persepallength)

persepalwidth=numpy.percentile(data[:,1],.8)
print('80th Percentile sepal width is',persepalwidth)

perpetallength=numpy.percentile(data[:,2],.8).round(2)
print('80th Percentile petal length is',perpetallength)

perpetalwidth=numpy.percentile(data[:,3],.8)
print('80th Percentile petal width is',perpetalwidth)

# calculate the median value in each column in the array
mediansepallength=numpy.median(data[:,0])
print('median sepal length is',mediansepallength)

mediansepalwidth=numpy.median(data[:,1])
print('median sepal width is',mediansepalwidth)

medianpetallength=numpy.median(data[:,2])
print('median petal length is',medianpetallength)

medianpetalwidth=numpy.median(data[:,3])
print('median petal width is',medianpetalwidth)

# calculate the standard deviation of each column in the array
sdsepallength=numpy.std(data[:,0]).round(2)
print('SD sepal length is',sdsepallength)

sdsepalwidth=numpy.std(data[:,1]).round(2)
print('SD sepal width is',sdsepalwidth)

sdpetallength=numpy.std(data[:,2]).round(2)
print('SD petal length is',sdpetallength)

sdpetalwidth=numpy.std(data[:,3]).round(2)
print('SD petal width is',sdpetalwidth)
