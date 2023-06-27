### Custom Exceptions ###

## Multiple exceptions
# You can use multiple except clauses to handle different exceptions separately. Each except clause specifies the type of exception it can handle
try:
    print(1 + 1)
except ValueError:
    print("FileNotFoundError")
except FileNotFoundError:
    print("except FileNotFoundError")
except Exception as e:
    print("Exception")


## Multiple exceptions grouped
# You can handle multiple exceptions using a single except clause by specifying the exceptions as a tuple
try:
    print(1 + 1)
except (ValueError, FileNotFoundError):
    print("ValueError or FileNotFoundError")


## Exception Hierarchy 
# Exceptions in Python are organized in a hierarchy, where some exceptions are subclasses of others.
# You can handle exceptions based on their hierarchical relationships
try:
    print(1 + 1)
except IOError:
    print("Handle IOError")
except OSError:
    # Code is unreachable because it will always raise IOError
    print("Handle OSError, which is a subclass of IOError")
except Exception:
    print("Handle any other exception")


## Exceptions Details
# You can access additional details about an exception using the as keyword. The exception instance can be assigned to a variable for further examination.
try:
    print(1 + 1)
except ValueError as e:
    print(f"Error: {e}")


## Exceptions clause
# You can include an else clause after the try-except block, which is executed if no exceptions are raised. It is typically used for code that should run when no exceptions occur.
try:
    print(1 + 1)
except ValueError:
    print("ValueError")
except FileNotFoundError:
    print("FileNotFoundError")
else:
    print("Else clause")


## Finally clause
# The finally clause is executed regardless of whether an exception occurred or not. It is commonly used for cleaning up resources or releasing acquired locks
try:
    print(1 + 1)
except ValueError:
    print("ValueError")
finally:
    print("Finally")


## Manual raise
# You can raise exceptions explicitly using the raise statement. This allows you to raise specific exceptions at desired points in your code. 
if 1 == 1:
    raise ValueError("Invalid condition")


