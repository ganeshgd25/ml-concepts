import statistics

# find mean 
number = [2,5,6,7,9,10,13,14,15,16,17]
mean = sum(number) // len(number)
print("Mean" , mean)

# fie median 
numbers = [1, 2, 3, 4, 5, 6]
print("Median" ,statistics.median(numbers))

numbers = [1, 2, 3, 4, 5 ]
print("Median" ,statistics.median(numbers))

# find mode 
no = [1,2,3,3,2,3,2,3,4,5,6,7,7,8,9,2,3]
print("Mode",statistics.mode(no))

# standard devaiataion
numbers = [10, 12, 23, 23, 16, 23, 21, 16]
print("Standard Deviation:", statistics.stdev(numbers))
print(statistics.mean(numbers))