'''Program is for problem J3 from 2008 CCC'''

phrase = input()

def calculate_movements(phrase):
    grid = [['A', 'B', 'C', 'D', 'E', 'F'],
            ['G', 'H', 'I', 'J', 'K', 'L'],
            ['M', 'N', 'O', 'P', 'Q', 'R'],
            ['S', 'T', 'U', 'V', 'W', 'X'],
            ['Y', 'Z', ' ', '-', '.', 'enter']]

    cursor = [0, 0]  # Starting position of the cursor
    movements = 0

    for char in phrase:
        target = None
        for i in range(len(grid)):
            for j in range (len(grid[i])):
                if char==grid[i][j]:
                    target = [i, j]
                    break
            if target is not None:
                break
        movements += abs(target[0]-cursor[0]) + abs(target[1]-cursor[1])
        cursor = target
    movements += abs(cursor[0]-4) + abs(cursor[1]-5)

    return movements

print(calculate_movements(phrase))