import numpy as np
data = np.array(np.random.randint(1, 100, size=25)).reshape(5,5)
print(data)

#Swap the second and fourth rows of the data matrix.
data[[1,3],:] = data[[3,1],:]
print(data)

#Normalize all the elements in the data matrix such that they are scaled to range between 0 and 1.
min = np.min(data)
max = np.max(data)
normalize = np.round((data - min)/ max,2)
print(normalize)
