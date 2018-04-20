# Mike Quaid 19042018

import numpy # numpy is a package or library of functions

data=numpy.genfromtxt('iris.txt',delimiter=',',dtype=float) # read data file into an array

# each element of the array is seperated by a comma in the raw data file
# the first column is [:,0]
# the first row is [0]

# calculate the mean of each column in the array
meansepallength=numpy.mean(data[:,0]) 
print('mean sepal length ',meansepallength)

meansepalwidth=numpy.mean(data[:,1]) 
print(round(meansepalwidth),2)

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

# calculate the minimum value in each column in the array
minsepallength=numpy.min(data[:,0])
print(minsepallength)

minsepalwidth=numpy.min(data[:,1])
print(minsepalwidth)

minpetallength=numpy.min(data[:,2])
print(minpetallength)

minpetalwidth=numpy.min(data[:,3])
print(minpetalwidth)

# calculate the percentile value in each column in the array
persepallength=numpy.percentile(data[:,0],.5)
print(persepallength)

# calculate the median value in each column in the array
mediansepallength=numpy.median(data[:,0])
print(mediansepallength)

mediansepalwidth=numpy.median(data[:,1])
print(mediansepalwidth)

medianpetallength=numpy.median(data[:,2])
print(medianpetallength)

medianpetalwidth=numpy.median(data[:,3])
print(medianpetalwidth)

# calculate the standard deviation of each column in the array
sdsepallength=numpy.std(data[:,0])
print(sdsepallength)

sdsepalwidth=numpy.std(data[:,1])
print(sdsepalwidth)

sdpetallength=numpy.std(data[:,2])
print(sdpetallength)

sdpetalwidth=numpy.std(data[:,3])
print(sdpetalwidth)
