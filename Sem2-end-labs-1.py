# Author: ATN 1/24/22

# Build Tower 6kyu

# this one was difficult
def tower_builder(n_floors):
    # i decided to make a variable called counter, which will represent the number of spaces each tower
    counter = n_floors - 1
    # because a tower of 1 will not have any spaces, we must make sure to set this
    if n_floors == 1:
        counter = 0
    # tower will be an empty list for now
    tower = []
    # this variable will represent the number of * in each layer of the tower
    per = 1
    # this for loop needs to begin with 1 and end with 1 plus the number of floors specified
    for x in range(1, n_floors + 1):
        # i used the string format method to easily add the positioning of the spaces for the tower
        tower.append("{0}{1}{0}".format(" " * counter, "*" * per))
        # after each iteration, the number of spaces will decrease by one and the number per tower layer will increase by 2
        counter -= 1
        per += 2
        continue
    return tower


print(tower_builder(3) == ['  *  ', ' *** ', '*****'])
print(tower_builder(1) == ['*'])
print(tower_builder(0) == [])