### LOOPING ###
## Breaking a for ##
names = ["Alice", "Bob", "Charlie", "Dave"]

for name in names:
    if name == "Charlie":
        # Here we gonna break the loop after found the value we were looking for.
        print("Found Charlie. Breaking loop.")
        break
    print(name)
else:
    print("End of the list.")


## Continuing a while ##
counter = 0
while counter < 5:
    counter += 1
    if counter == 3:
        # Here we use continue to skip all next lines and go ahead to next while interaction
        print("Found number 3. Going to the next interation...")
        continue
    print(counter)
else:
    print("End of the loop.")


## Using pass in a loop ##
for i in range(5):
    # This is an empty block
    pass
