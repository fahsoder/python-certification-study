### Exceptions & errors ###
## Try ## 
try:
    # Code that might raise an exception
    result = 10 / 0  # Division by zero - raises ZeroDivisionError
except ZeroDivisionError:
    # Custom error handling code
    print("Error: Division by zero is not allowed.")


## Multiple Except Clauses ##
try:
    # Code that might raise exceptions
    file = open("myfile.txt", "r")
    content = file.read()
    num = int(content)
except FileNotFoundError:
    print("Error: File not found.")
except ValueError:
    print("Error: Invalid integer value.")


## Finally ##
try:
    # Code that might raise an exception
    file = open("myfile.txt", "r")
    # Process the file content
finally:
    # Cleanup code
    file.close()


## Raise an error ## 
age = -10
if age < 0:
    raise ValueError("Invalid age: Age cannot be negative.")
