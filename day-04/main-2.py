total_copies = 0
matrix = []
card_copies = []

def read_cards():
    global total_copies, card_copies

    for i in range(len(matrix)):
        line = matrix[i]
        current_card = i + 1
        current_card_copies = 1
        winning = []
        ours = []

        # check if this card has copies
        for cc in range(len(card_copies)):
            for copy in card_copies[cc]:
                # add to the current amount of card copies
                if current_card == copy:
                    current_card_copies += 1

        # get winning nums
        winning = get_winners(line)
        # get our nums
        ours = get_ours(line)

        # save card copies
        for copies in range(current_card_copies):
            get_card_copies(current_card, winning, ours)
            total_copies += 1

        
def get_card_copies(current_card, winning, ours):
    global card_copies
    line_copies = []
    line_matches = 0

    # check this card winning nums
    for num in ours:
        if num in winning:
            line_matches += 1
    
    # save card copies won from current card
    for j in range(line_matches):
        line_copies.append(current_card + (line_matches - j))

    card_copies.append(line_copies)


def get_winners(line):
    winning = []
    for w in line.split("|")[0].strip().split(" "):
            if (w != ""):
                winning.append(w)
    return winning


def get_ours(line):
    ours = []
    for o in line.split("|")[1].strip().split(" "):
        if (o != ""):
            ours.append(o)
    return ours


def readInput():
    with open('input.txt') as input:
        for line in input.readlines():
            matrix.append(line.split(":")[1].strip())
    
    read_cards()
    
    print('-------RESULT-------')
    print(total_copies)
    print('--------------------')

readInput()