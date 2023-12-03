import math as m, re

gear_ratios = 0
matrix = []

def calc_parts():
    global gear_ratios

    # get symbols position dict
    symbols = {}
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] in '*':
                symbols[(r, c)] = []

    for r, row in enumerate(matrix):
        for num in re.finditer(r'\d+', row):
            # find matrix adjacent positions
            edge = {
                (r, c) 
                    for r in (r-1, r, r+1) 
                    for c in range(num.start()-1, num.end()+1)
            }

            for e in edge:
                for s in symbols.keys():
                    if (e == s):
                        symbols[e].append(int(num.group()))
    
    for k, value in symbols.items():
        gear_ratio = 0
        if (len(value) == 2):
            gear_ratio = value[0] * value[1]
        gear_ratios += gear_ratio

def readInput():
    with open('input.txt') as input:
        for line in input.readlines():
            matrix.append(line)
    
    calc_parts()
    
    print('-------RESULT-------')
    print(gear_ratios)
    print('--------------------')

readInput()