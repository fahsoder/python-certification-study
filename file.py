import os
### File ###

## Reading ##
# Reading the entire file
with open("file.txt", "r") as file:
    content = file.read()
    print(content)

# Reading the file line by line
with open("file.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line)


## Writing ## 
# Writing to a file
with open("file.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample text.")


## Directory ##
# Create a directory
os.mkdir("mydir")

# List files and directories in a directory
files = os.listdir("mydir")
for file in files:
    print(file)

# Join directory paths
path = os.path.join("mydir", "subdir", "file.txt")
print(path)

# Remember to handle exceptions, such as FileNotFoundError or PermissionError, when working with files and directories.