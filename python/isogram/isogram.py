from string import ascii_lowercase


def is_isogram(string):
    string = string.lower()
    for letter in ascii_lowercase:
        count = 0
        for x in string:
            if letter == x:
                count += 1
            if count > 1:
                return False

    return True
