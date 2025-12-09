import numpy as np

# 1. list of numbers
numbers = [10, 23, 5, 8, 15]

# 2. Converting numbers into numpy array
arr = np.array(numbers)

# 3. Calculating mean, maximum, sum
mean_value = np.mean(arr)
max_value = np.max(arr)
sum_value = np.sum(arr)

# 4. Print the results
print("Numbers:", numbers)
print("As NumPy array:", arr)
print("Mean:", mean_value)
print("Maximum value:", max_value)
print("Sum:", sum_value)
