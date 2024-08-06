def rotate(text, key):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_lowercase = lowercase[key:] + lowercase[:key]
    new_uppercase = uppercase[key:] + uppercase[:key]

    new_text = ""
    for c in text:
        if c in lowercase:
            new_text += new_lowercase[lowercase.index(c)]
        elif c in uppercase:
            new_text += new_uppercase[uppercase.index(c)]
        else:
            new_text += c

    return new_text

