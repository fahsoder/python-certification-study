### LISTS ###
fruit_list = ['apple', 'banana', 'orange']
print(fruit_list[0])  # output: apple
fruit_list.append('strawberry')
print(fruit_list)  # output: ['apple', 'banana', 'orange', 'strawberry']


### TUPLES ###
color_tuple = 'red', 'green', 'blue'
print(color_tuple[1])  # output: green
# color_tuple[0] = 'yellow'  # Would raise an error because tuples are not mutable


### SETS ###
number_set = {1, 2, 3, 4, 4, 5}
print(number_set)  # output: {1, 2, 3, 4, 5}
number_set.add(6)
print(number_set)  # output: {1, 2, 3, 4, 5, 6}
number_set.add(3)
print(number_set)  # output: {1, 2, 3, 4, 5, 6}
number_set.add('test')
for i in number_set:
    print(i)

# print(number_set[0])  # Error! Sets are not subscriptable, cannot be accessed by indices
# obj_set = {dict({'name': 'Soder', 'phone': '123'})} # Would raise an error because dicts are mutables and set items cannot be mutable