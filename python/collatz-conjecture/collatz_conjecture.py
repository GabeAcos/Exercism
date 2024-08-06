def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    number_of_steps = 0
    while 1 != number:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1
        number_of_steps += 1
    return number_of_steps
