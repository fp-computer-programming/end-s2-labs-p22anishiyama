# Author: ATN 1/24/22

# Take a Ten Minute Walk 6kyu

def is_valid_walk(walk):
    # returns true if the list of walk has exactly 10 directions, and each direction will result into overall change in position
    return True if len(walk) == 10 and (walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')) else False
    # i managed to solve this one in one line

print(is_valid_walk(['n', 's', 'e', 'w', 'w', 'e', 's', 'n', 'e', 'w']))
print(is_valid_walk(['s', 'n', 'e', 'w', 's', 'n', 'w', 'e', 'n', 's']))
print(is_valid_walk(['s', 's', 's', 's', 's', 'n', 'n', 'n', 'n', 'n']))
