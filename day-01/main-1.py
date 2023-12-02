calibration = 0

def get_calibrations(line):
    global calibration
    lineNums = []

    for c in line:
        if c.isdigit():
            lineNums.append(c)

    cal = str(lineNums[0]) + str(lineNums[-1])
    calibration += int(cal)


def readInput():
    with open('/Users/p1vergara/Repositorio/aoc-2023/day-01/input.txt') as input:
        for line in input.readlines():
            get_calibrations(line)
    
    print('-------RESULT-------')
    print(calibration)
    print('--------------------')

readInput()