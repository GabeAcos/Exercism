def square_of_sum(number):
    sum = 0
    for num in range(number + 1):
        sum += num
    return sum ** 2


def sum_of_squares(number):
    sum = 0
    for num in range(number + 1):
        sum += num ** 2
    return sum

def difference_of_squares(number):
    return abs(sum_of_squares(number) - square_of_sum(number))
