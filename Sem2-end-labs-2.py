# Author: ATN 1/24/22

# Duplicate Encoder 6kyu

def duplicate_encode(word):
    # i began by making sure there are no capitals in this word as it will simplify this function drastically
    word = word.lower()
    # i set encode as a blank string so i am able to add to it during my for loop
    encode = ""
    for x in word:
        # if the occurances of this letter are greater than one, add ), else (
        if word.count(x) > 1:
            encode += ")"
            continue
        else:
            encode += "("
            continue
    return encode

print(duplicate_encode("test") == ')(()')
print(duplicate_encode("aiden") == '(((((')
print(duplicate_encode("this is a very very long test") == ')())))))()))))))))))(((()))))')
