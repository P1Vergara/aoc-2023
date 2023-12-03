calibration = 0
numsToInt = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

def replace_nums(line):
    formated_line = line
    for k, v in numsToInt.items():
        formated_line = formated_line.replace(k, v)
    
    return formated_line

def get_calibrations(line):
    global calibration

    formated = replace_nums(line)
    lineNums = []

    for c in formated:
        if c.isdigit():
            lineNums.append(c)

    cal = str(lineNums[0]) + str(lineNums[-1])
    calibration += int(cal)


def readInput():
    with open('input.txt') as input:
        for line in input.readlines():
            get_calibrations(line)
    
    print('-------RESULT-------')
    print(calibration)
    print('--------------------')

readInput()