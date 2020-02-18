from hf1 import max_pooling
from hf2 import flea_jump
from hf3 import ran
from hf4 import is_there_braking,number_of_brakings
import numpy as np

# TEST HF1
input_table = [
 [1,2,3,4,5,6,7,8,9,10],
 [2,3,4,5,6,7,8,9,10,1],
 [3,4,5,6,7,8,9,10,1,2],
 [4,5,6,7,8,9,10,1,2,3],
 [5,6,7,8,9,10,1,2,3,4],
 [6,7,8,9,10,1,2,3,4,5],
 [7,8,9,10,1,2,3,4,5,6],
 [8,9,10,1,2,3,4,5,6,7],
 [9,10,1,2,3,4,5,6,7,8],
 [10,1,2,3,4,5,6,7,8,9]]

max_pooling(input_table)

# TEST HF2
flea_jump(3,4,"EEKDNK") # várható output (4,5)

# TEST HF3
ran()

# TEST HF4
measurement= np.array([0.4, 0.31, 0.81, 0.91, 0.76, 0.24, 0.94, 0.28, 0.86, 0.99, 0.22])

threshold_1 = 0.75
print('Is there braking?', is_there_braking(measurement, threshold_1), 'for threshold', threshold_1) # Response: True
threshold_2 = 0.77
print('Is there braking?', is_there_braking(measurement, threshold_2), 'for threshold', threshold_2) # A válasz: nincs

measurement = np.array([0.32, 0.88, 0.55, 0.76, 0.81, 0.93, 0.11, 0.99, 0.87, 0.79, 0.90, 0.82, 0.67, 0.21, 0.78, 0.93, 0.12, 0.97, 0.95, 0.89, 0.31, 0.78, 0.79, 0.55])
threshold = 0.75

print('Number of brakings:', number_of_brakings(measurement, threshold), 'for threshold', threshold) # Output: 3