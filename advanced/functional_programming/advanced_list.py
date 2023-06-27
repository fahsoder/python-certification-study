### Advanced List Comprehensions ###

## Filtering with For ##
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6]


## Mapping with Transformation ##
names = ["Alice", "Bob", "Charlie"]
name_lengths = [len(name) for name in names]
print(name_lengths)  # Output: [5, 3, 7]


## Nested List Comprehensions ##
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [element for row in matrix for element in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


## Conditional Transformation ##
numbers = [1, 2, 3, 4, 5]
result = [x ** 2 if x % 2 == 0 else x for x in numbers]
print(result)  # Output: [1, 4, 3, 16, 5]


## Testing a way to work with any matrix level ##
m = [[1, 2, 3], [1, 3], [1, 2, 3], [1, [1, 2, [1, 3]]]]
r = lambda a: list(set([element for row in a for element in (r(row) if isinstance(row, list) else [row])]))
print(r(m)) # Output: [1, 2, 3]
