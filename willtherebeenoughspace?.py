# Will there be enough space? 8 kyu

def enough(cap, on, wait):
    amount = (on + wait) - cap
    if amount > 0:
        return amount
    else:
        return 0
