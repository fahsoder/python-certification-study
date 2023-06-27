### Python code structure ###
# Python is based on code identation to especify new lines and code blocks
# Functions must be declared before they are used, otherwise the code will raise an erro like the function is not declared

### Diff between dict and list ###
# Lists allow you to append new object with any format
li = list(['test', {'values': [{'test': 'test2'}, {'test': 'test3'}]}, 'test2'])

# Dicts were made to append just itens that follow the key:value format - Like a Hashmap
# The code below will run because it contains only objects which has key:value format
di = dict({'values': [{'test': 'test2'}, {'test': 'test3'}]})

# The code below will raise an error because the format doesnt follow the key:value rule
# di2 = dict(['test2', 'test2', {'values': [{'test': 'test2'}, {'test': 'test3'}]}])

# Checkout the diference between list and dict using print command
print(li)
print(di)


### Event looping ###
# item = []
# for i in item:
#   do x;

