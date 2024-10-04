def number(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * number(base, exponent - 1)


try:
    