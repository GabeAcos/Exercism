# Constants
COLOR_DICT = {'black': '0', 'brown': '1', 'red': '2', 'orange': '3',
              'yellow': '4', 'green': '5', 'blue': '6', 'violet': '7',
              'grey': '8', 'white': '9'}

METRIC_LIST = ['', 'kilo', 'mega', 'giga', 'tera', 'peta', 'exa']

TOLERANCE_DICT = {'grey': '0.05%', 'violet': '0.1%', 'blue': '0.25%',
                  'green': '0.5%', 'brown': '1%', 'red': '2%', 'gold': '5%',
                  'silver': '10%'}


# Helper Functions
def value(colors):
    val = ""
    for color in colors:
        val += COLOR_DICT[color]
    return int(val)


def magnitude(magnitude_color):
    return int(COLOR_DICT[magnitude_color]) * "0"

def dot_zero(number):
    if str(number).endswith('.0'):
        return int(number)
    else:
        return number

# Main function
def resistor_label(colors):
    if len(colors) == 1:
        return("0 ohms")
    elif len(colors) == 4:
        val = str(value(colors[:2])) + magnitude(colors[2])
        tol = TOLERANCE_DICT[colors[3]]
        metric_prefix = ""
        if len(val) > 3:
            metric_prefix = METRIC_LIST[len(val) // 3]
        val = int(val) * (10 ** (METRIC_LIST.index(metric_prefix) * -3))
        val = dot_zero(val)
        return f"{val} {metric_prefix}ohms ±{tol}"
    else:
        val = str(value(colors[:3])) + magnitude(colors[3])
        tol = TOLERANCE_DICT[colors[4]]
        metric_prefix = ""
        if len(val) > 3:
            metric_prefix = METRIC_LIST[len(val) // 3]
        val = int(val) * (10 ** (METRIC_LIST.index(metric_prefix) * -3))
        val = round(dot_zero(val),3)
        return f"{val} {metric_prefix}ohms ±{tol}"

