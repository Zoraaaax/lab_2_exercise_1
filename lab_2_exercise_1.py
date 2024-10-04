def number(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * number(base, exponent - 1)


try:
    base = int(input("Enter the base: "))
    exponent = int(input("Enter the exponent: "))
    