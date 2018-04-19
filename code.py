# Mike Quaid 19042018

import numpy # numpy is a package or library of functions

data=numpy.genfromtxt('iris.txt',delimiter=',') # read data file into an array

# each element of the array is seperated by a comma in the raw data file
# the first column is [:,0]
# the first row is [0]

# calculate the mean of each column in the array
meanfirstcol=numpy.mean(data[:,0]) 
print(meanfirstcol)

meansecondcol=numpy.mean(data[:,1]) 
print(meansecondcol)

meanthirdcol=numpy.mean(data[:,2]) 
print(meanthirdcol)

meanfourthcol=numpy.mean(data[:,3]) 
print(meanfourthcol)

# calculate the maximum value in each column in the array
maxfirstcol=numpy.max(data[:,0])
print(maxfirstcol)

maxsecondcol=numpy.max(data[:,1])
print(maxsecondcol)

maxthirdcol=numpy.max(data[:,2])
print(maxthirdcol)

maxfourthcol=numpy.max(data[:,3])
print(maxfourthcol)
