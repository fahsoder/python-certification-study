### String Formation ###

## Concatenation ##
name = "Alice"
age = 30
greeting = "Hello, " + name + "! You are " + str(age) + " years old."
print(greeting)

# Using the % operator: This operator allows you to format strings using placeholders
name = "Bob"
age = 25
greeting = "Hello, %s! You are %d years old." % (name, age)
print(greeting) 

# Using the str.format() method: This method provides more flexibility and readability for string formatting
name = "Charlie"
age = 35
greeting = "Hello, {}! You are {} years old.".format(name, age)
print(greeting)

# Using f-strings (formatted string literals): Introduced in Python 3.6, f-strings offer a concise and intuitive way to format strings
name = "David"
age = 40
greeting = f"Hello, {name}! You are {age} years old."
print(greeting)
