COLOR_DICT = {'black': '0', 'brown': '1', 'red': '2', 'orange': '3',
              'yellow': '4', 'green': '5', 'blue': '6', 'violet': '7',
              'grey': '8', 'white': '9'}

METRIC_LIST = ['', 'kilo', 'mega', 'giga', 'tera', 'peta', 'exa']


def value(colors):
    return int(COLOR_DICT[colors[0]] + COLOR_DICT[colors[1]])

def zeros(color):
    return int(COLOR_DICT[color]) * "0"

def metric(val):
    amount_zeros = 0
    metric_prefix = ''
    for x in val:
        if x == '0':
            amount_zeros += 1
    if amount_zeros > 2:
        metric_prefix = METRIC_LIST[amount_zeros//3]
        val = val[:(amount_zeros//3 * -3)]
    return val, metric_prefix
def label(colors):
    val = str(value(colors[:2])) + zeros(colors[2])
    metric_prefix = ''
    val, metric_prefix = metric(val)
    return(val + " " + metric_prefix + "ohms")


