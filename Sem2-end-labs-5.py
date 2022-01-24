# Author: ATN 1/24/22

# Who likes it? 6kyu

# this is a basic conditional which adds a list of users who like a post, similar to facebook
def likes(names):
    # i am setting the list of names to x, which will act as the length of the list, resulting in an easier comparison
    x = len(names)
    # if the length of the list meets the criteria, i will format the string accordingly
    if(x == 0):
        return "no one likes this"
    elif(x == 1):
        return "{0} likes this".format(names[0])
    elif(x == 2):
        return "{0} and {1} like this".format(names[0], names[1])
    elif(x == 3):
        return "{0}, {1} and {2} like this".format(names[0], names[1], names[2])
    else:
        return ("{0}, {1} and {2} others like this".format(names[0], names[1], x - 2))


print(likes(['James', 'Aiden']) == 'James and Aiden like this')
print(likes([]) == 'no one likes this')
print(likes(['Aiden']) == 'Aiden likes this')
