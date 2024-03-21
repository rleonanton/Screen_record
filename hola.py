import numpy as np

list1 = [1,2,3,4,5,6]

list2 = ["Jhon", 41, list1, True]

np1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(np1)
print(np1.shape)

#Range
np2 = np.arange(10)
print(np2)

#Step
np3 = np.arange(0,50,2)
print(np3)

#Zeros
np4 = np.zeros(10)
print(np4)

#multidimensional
np5 = np.zeros((2,10))
print(np5)

#Full Function
np6 = np.full((10),6)
print(np6)

#Multidimensional
np7 = np.full((2,10),6)
print(np7)

