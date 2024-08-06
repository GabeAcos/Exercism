def is_valid(isbn):
    new_isbn = isbn.replace('-', '')
    if len(new_isbn) != 10:
        return False

    multiplier = 10
    total_sum = 0
    for digit in new_isbn:
        if digit.isdigit():
            total_sum += int(digit) * multiplier
            multiplier -= 1
        elif digit == "X":
            total_sum += 10
        else:
            return False

    return total_sum % 11 == 0
