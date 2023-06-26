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
