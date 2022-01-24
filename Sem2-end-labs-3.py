# Author: ATN 1/24/22

# Create Phone Number 6kyu

def create_phone_number(n):
    # i set new_n to list out each number given as a list
    new_n = [str(x) for x in n]
    # i then added 3 blank strings which will organize the phone number into 3 individual components
    first = ""
    second = ""
    third = ""
    # i then organized each of the blank strings into their respective numbers
    for x in new_n[0:3]: first += x
    for x in new_n[3:6]: second += x
    for x in new_n[6:10]: third += x
    # the user is now able to retrieve my formatted strings
    return "({0}) {1}-{2}".format(first, second, third)


# these tests are just random numbers i typed
print(create_phone_number('1234567891'))
print(create_phone_number('3476546566'))
print(create_phone_number('2035634562'))
