def is_armstrong_number(number):
    number_string = str(number)
    sum_of_digits = 0
    power = len(number_string)
    for index in range(len(number_string)):
        sum_of_digits += int(number_string[index]) ** power

    return sum_of_digits == number
    # if sum_of_digits == number:
    #     return True
    # else:
    #     return False
