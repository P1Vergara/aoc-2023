game_power_sum = 0

def check_cubes(line):
    global game_power_sum

    games = line.split(":")
    sets = games[1].split(";")
    set_blues = []
    set_reds = []
    set_greens = []

    for s in sets:
        cubes = s.split(",")
        blue_cubes = 0
        red_cubes = 0
        green_cubes = 0

        for cube in cubes:
            c = cube.strip().split(" ")
            if "blue" in c[1]:
                blue_cubes += int(c[0])
            if "red" in c[1]:
                red_cubes += int(c[0])
            if "green" in c[1]:
                green_cubes += int(c[0])
        
        set_blues.append(blue_cubes)
        set_reds.append(red_cubes)
        set_greens.append(green_cubes)
        
    game_power_sum += (max(set_blues) * max(set_reds) * max(set_greens))

def readInput():
    with open('/Users/p1vergara/Repositorio/aoc-2023/day-02/input.txt') as input:
        for line in input.readlines():
            check_cubes(line)
    
    print('-------RESULT-------')
    print(game_power_sum)
    print('--------------------')

readInput()