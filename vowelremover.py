# Vowel remover 8 kyu

def shortcut( s ):
    vowels = ["a", "e", "i", "o", "u"]
    for letter in  list(s):
        if(letter in vowels):
            s = s.replace(letter, "")
            continue
    return s