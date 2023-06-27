### REGEX ###

# Importing lib 're'
import re

## Match ##
text = "Hello, World!"
pattern = r"Hello"
match =  lambda x, y: "Pattern found!" if (re.search(x, y)) else "Pattern not found!"
print(match(pattern, text)) # Output: Pattern found!


## Extracting Substrings ##
text = "My email is example@example.com and we got this fahsoder@gmail.com and this incorrent one fahsoder@gmail"
pattern = r"\b\w+@\w+\.\w+\b"
matches = lambda x, y: [element for element in (re.findall(x, y))]
print(matches(pattern, text)) # Output: ['example@example.com', 'fahsoder@gmail.com']


## Replacing Patterns ##
text = "Hello, World!"
pattern = r"Hello"
replacement = "Hi"
new_text = re.sub(pattern, replacement, text)

print(new_text)  # Output: "Hi, World!"
