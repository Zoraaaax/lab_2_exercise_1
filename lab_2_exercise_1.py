def number(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * number(base, exponent - 1)


try:
    base = int(input("Enter the base: "))
    exponent = int(input("Enter the exponent: "))
    result = number(base, exponent)
    print(f"The result of {base} raised to the power of {exponent} is {result}")

except ValueError:
    print("Invalid input. Please enter valid integers for base and exponent.")
