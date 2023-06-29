### Pathlib ###

from pathlib import Path

## Path Creation And Access
# Create a Path object representing a file
file_path = Path('path/to/file.txt')

# Create a Path object representing a directory
dir_path = Path('path/to/directory')

# Get the current working directory
current_dir = Path.cwd()

# Get the user's home directory
home_dir = Path.home()


## Path Operations
file_path = Path('path/to/file.txt')

# Access the parent directory
parent_dir = file_path.parent

# Get the name of the file or directory
name = file_path.name

# Get the file extension
extension = file_path.suffix

# Get the file name without the extension
stem = file_path.stem

# Check if the path exists
exists = file_path.exists()

# Check if the path points to a regular file
is_file = file_path.is_file()

# Check if the path points to a directory
is_dir = file_path.is_dir()

# Get the absolute path
absolute_path = file_path.absolute()


## File & Directory Manipulation
file_path = Path('path/to/file.txt')
dir_path = Path('path/to/directory')

# Rename the file or directory
file_path.rename('new_name.txt')

# Remove/delete the file or directory
file_path.unlink()

# Create a new directory
dir_path.mkdir()

# Remove/delete an empty directory
dir_path.rmdir()

# Find files and directories matching a glob pattern
for path in dir_path.glob('*.txt'):
    print(path)

# Iterate over all files and directories in a directory
for item in dir_path.iterdir():
    print(item)


## Path concatenation and resolution
base_path = Path('path/to')
subdir_path = base_path / 'subdir'
print(subdir_path)  # path/to/subdir

# Resolve the path to its absolute form
absolute_path = subdir_path.resolve()
print(absolute_path)
