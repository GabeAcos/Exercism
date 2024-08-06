def answer(question):
    # helper function used to operation in the for loop at the end
    def operate(a, operation, b):
        if operation == 'plus':
            return a + b
        elif operation == 'minus':
            return a - b
        elif operation == 'multiplied':
            return a * b
        elif operation == 'divided':
            return a / b

    valid_operators = ['plus', 'minus', 'multiplied', 'divided']

    # Starting cleanup
    if "What is" not in question:
        raise ValueError("unknown operation")

    # Cleaning up the question, removing words and punctuation, then splitting the remained into a list of strings
    question = question[:-1].replace("What is", "").replace("by", "").split()

    # Next section is dealing with invalid questions
    if valid_operators not in question:
        if len(question) == 1:
            try:
                return float(question[0])
            except:
                raise ValueError("syntax error")

    if 'cubed' in question:
        raise ValueError("unknown operation")

    if len(question) == 0:
        raise ValueError("syntax error")

    try:
        int(question[0])
    except:
        if question[0] in valid_operators:
            raise ValueError("syntax error")
        else:
            raise ValueError("unknown operation")
    # End of cleanup

    # The remainder should be in the format of number, operator, number...
    final_answer = question[0]
    for i in range(1, len(question), 2):
        try:
            final_answer = operate(int(final_answer), question[i], int(question[i + 1]))
        except:
            raise ValueError("syntax error")

    return final_answer
