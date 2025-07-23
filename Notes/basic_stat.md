# statistics for machine learning

# 1. Mean (Average)
Definition:
Sum of all numbers divided by count of numbers.

Formula:

Mean= Number of values /Sum of all values

Example:
Numbers: 2, 4, 6, 8

Mean=(2+4+6+8)/4=5

# python code
numbers = [2, 4, 6, 8]
mean = sum(numbers) / len(numbers)
print("Mean:", mean)


# 2. median middle value

# Definition:
The middle number when data is sorted.

Odd count → middle value

Even count → average of two middle values

# Example:
Numbers: 1, 2, 3, 4, 5 → Median = 3
Numbers: 1, 2, 3, 4 → Median = (2+3)/2 = 2.5


# python code
import statistics
numbers = [1, 2, 3, 4, 5]
print("Median:", statistics.median(numbers))


# 3. Mode 
# Definition:
The value that appears most often.

# Example:
Numbers: 1, 2, 2, 3, 4 → Mode = 2

# python code
import statistics
numbers = [1, 2, 2, 3, 4]
print("Mode:", statistics.mode(numbers))

# 4. standard Deviation
# Definition:
Tells how far the numbers are from the average (mean).

Small SD: values are close to the mean

Large SD: values are far apart

# Example Data:
10, 12, 23, 23, 16, 23, 21, 16

Mean = 18

Standard Deviation ≈ 5.24

# python code
import statistics
numbers = [10, 12, 23, 23, 16, 23, 21, 16]
print("Standard Deviation:", statistics.stdev(numbers))
