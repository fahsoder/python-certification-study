### File and Directory Commands ### 

# The os and shutil modules provide a wide range of functionalities to work with files and directories. 
# Allowing you to perform tasks such as copying, moving, deleting, and manipulating file and directory attributes.
import os
import shutil

path = './'
src = path + 'src'
dst = path + 'dst'
mode = 'mode'

## File and Directory Navigation
os.getcwd() # Get the current working directory.
os.chdir(path) # Change the current working directory to the specified path.
os.path.abspath(path) # Get the absolute path of a file or directory.
os.path.exists(path) # Check if a file or directory exists.


## File Operations
os.path.isfile(path) # Check if a path points to a regular file.
os.path.getsize(path) # Get the size of a file in bytes.
os.remove(path) # Remove/delete a file.
shutil.copy(src, dst) # Copy a file from the source path to the destination path.
shutil.move(src, dst) # Move/rename a file from the source path to the destination path.

## Directory Operations 
os.mkdir(path) # Create a new directory at the specified path
os.makedirs(path) # Create a new directory and any necessary intermediate directories
os.rmdir(path) # Remove/delete an empty directory.
shutil.rmtree(path) # Remove/delete a directory and its contents recursively.


## File and Directory Listing
os.listdir(path) # Get a list of all files and directories in a directory.
os.scandir(path) # Get an iterator of all files and directories in a directory.


## File and Directory Permissions
os.chmod(path, mode) # Change the permissions of a file or directory.
os.access(path, mode) # Check if a file or directory has the specified access permissions.


## File and Directory Metadata
os.stat(path) # Get the metadata (e.g., size, timestamps) of a file or directory.
os.path.getmtime(path) # Get the modification timestamp of a file or directory.