import numpy as np
array3= np.array([[['A', 'B', 'C'], ['D', 'E', 'F']],
                  [['G', 'H', 'I'], ['J', 'K', 'L']],
                  [['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X']]])
#array[start:end:step]
print(array3[0:3:2])
print(array3[::])
