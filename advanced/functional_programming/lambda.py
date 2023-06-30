### Lamba Functions ###

## Lambda function definition ##
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5

## Sorting with lambda ## 
fruits = ['apple', 'banana', 'cherry', 'date']
sorted_fruits = sorted(fruits, key=lambda x: len(x))
print(sorted_fruits)  # Output: ['date', 'apple', 'banana', 'cherry']

## Filtering with lambda ##
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

## Mapping with lambda ##
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

## Lambda Encapsulation ## 
def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
triple = multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15

## Functional Programming ##
numbers = [1, 2, 3, 4, 5]

# Example 1: Map and Filter
squared_numbers = list(map(lambda x: x ** 2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
print(even_numbers)     # Output: [2, 4]

# Example 2: Reduce
from functools import reduce
sum_of_numbers = reduce(lambda x, y: x + y, numbers)

print(sum_of_numbers)   # Output: 15

