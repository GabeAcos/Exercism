ACTIONS = ['wink', 'double blink', 'close your eyes', 'jump']


def reverse_binary(bin):
    l = []
    for x in range(len(bin) - 1,-1, -1):
        l.append(bin[x])
    return l


def commands(binary_str):
    handshake = []
    binary_list = reverse_binary(binary_str)
    for x in range(len(binary_list) - 1):
        if binary_list[x] == '1':
            handshake.append(ACTIONS[x])
    if binary_list[-1] == '1':
        handshake = list(reversed(handshake))

    return handshake
