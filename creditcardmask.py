# Credit Card Mask 7 kyu

# return masked string
def maskify(cc):
    value = "#" * (len(cc) - 4)
    last_four = cc[-4:]
    return (value + last_four)
