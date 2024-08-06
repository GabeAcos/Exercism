def square(number):
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    x = 0
    for i in range(64):
        x += 2 ** i
    return x
