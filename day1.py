'''
day 1 advent of code 2022 01/12/22
'''

import numpy as np
import pandas as pd

path = r'/home/natalie/Documents/Codes/advent22/'

# I saved the data to a csv because I love pandas
data = pd.read_csv(path + 'day1_data.csv')

# we need to sum each block of numbers and identify the index corresponding to the largest total

# first get the indices of the NaNs which divide the blocks
nans = data[data['calories'].isnull()]
nan_indices = nans.index.to_list()

# first entry is
total_calories = [data['calories'][0:nan_indices[0]].sum()]

# and loop to get the rest
# we turn it into a numpy array in the same step so we can use max() to find the largest number
total_calories = np.array([data['calories'][nan_indices[i]:nan_indices[i+1]].sum() for i in range(len(nan_indices) - 1)])

max_calories = total_calories.max()

# the answer to part one
print(max_calories)

# part two asks for the top 3 largest numbers, so we need to sort the total_calories array
# np.sort returns ascending order; minuses yield descending
sorted_total_calories = -np.sort(-total_calories)

top_three_max = sorted_total_calories[0:3]

total_top_three = sum(top_three_max)

print(total_top_three)
