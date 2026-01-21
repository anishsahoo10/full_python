import numpy as np
#1d Array
array = np.array(['A', 'B', 'C'])
print(array.ndim)

#2d Array
array2 = np.array([['A', 'B', 'C'], ['D', 'E', 'F']])
print(array2.ndim)
#3d Array
array3= np.array([[['A', 'B', 'C'], ['D', 'E', 'F']],
                  [['G', 'H', 'I'], ['J', 'K', 'L']],
                  [['M', 'N', 'O'], ['P', 'Q', 'R']]])
print(array3.ndim)
#chain indexing
print(array3[0][0][0])
#multidimentional indexing
print(array3[0,1,0]) #faaastest way

#word making
word = array3[0,0,0]+array3[0,1,0]+array3[0,0,1]+array3[0,1,1]+array3[0,1,2]
print(word)