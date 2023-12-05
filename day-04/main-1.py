points = 0
matrix = []

def calc_points():
    global points

    for line in matrix:
        counter = 1
        line_points = 0
        winning = []
        ours = []

        for w in line.split("|")[0].strip().split(" "):
            if (w != ""):
                winning.append(w)
        
        for o in line.split("|")[1].strip().split(" "):
            if (o != ""):
                ours.append(o)

        for num in ours:
            if num in winning:
                if (counter > 1):
                    line_points = line_points * 2
                else:
                    line_points = 1
                 
                counter += 1
        
        points += line_points


def readInput():
    with open('input.txt') as input:
        for line in input.readlines():
            matrix.append(line.split(":")[1].strip())
    
    calc_points()
    
    print('-------RESULT-------')
    print(points)
    print('--------------------')

readInput()