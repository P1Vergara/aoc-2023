import math as m, re

parts_sum = 0
matrix = []

def calc_parts():
    global parts_sum

    # get symbols position dict
    symbols = {}
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] not in '01234566789.':
                symbols[(r, c)] = []

    for r, row in enumerate(matrix):
        for num in re.finditer(r'\d+', row):
            # find matrix adjacent positions
            adjacent = {
                (r, c) 
                    for r in (r-1, r, r+1) 
                    for c in range(num.start()-1, num.end()+1)
            }

            for a in adjacent:
                for s in symbols.keys():
                    if (a == s):
                        symbols[a].append(int(num.group()))

    for k, value in symbols.items():
        for v in value:
            parts_sum += v

def readInput():
    with open('input.txt') as input:
        for line in input.readlines():
            matrix.append(line)
    
    calc_parts()
    
    print('-------RESULT-------')
    print(parts_sum)
    print('--------------------')

readInput()