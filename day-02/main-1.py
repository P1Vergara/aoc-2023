game_ids_sum = 0

def check_cubes(line):
    global game_ids_sum

    games = line.split(":")
    sets = games[1].split(";")
    possible_game = True

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
        
        
        if blue_cubes > 14 or red_cubes > 12 or green_cubes > 13:
            possible_game = False
    
    if possible_game:
        game_ids_sum += int(games[0].split(" ")[1])

def readInput():
    with open('input.txt') as input:
        for line in input.readlines():
            check_cubes(line)
    
    print('-------RESULT-------')
    print(game_ids_sum)
    print('--------------------')

readInput()