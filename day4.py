def check_xmas(lines, i, j, i_dir, j_dir):

    # Given a starting position (i,j) and directions (1 for increasing, -1 for decreasing, 0 for no change)
    # determine if "MAS" is spelled (assumes the starting point is already known to be "X")
    if i_dir == -1 and i < 3:
        return False
    if i_dir == 1 and i >= len(lines) - 3:
        return False 
    if j_dir == -1 and j < 3:
        return False
    if j_dir == 1 and j >= len(lines[0]) - 3:
        return False

    return lines[i+i_dir*1][j+j_dir*1] == 'M' and \
           lines[i+i_dir*2][j+j_dir*2] == 'A' and \
           lines[i+i_dir*3][j+j_dir*3] == 'S'


with open("C:/Python/2024/day4input.txt", 'r') as file:

    lines = [line.strip() for line in file]
   
    countP1 = 0
    for i,line in enumerate(lines):
        for j,el in enumerate(line):
            if el == 'X':
                for i_dir in range(-1,2):
                    for j_dir in range(-1,2):
                        # Given that this element is X, check all 8 directions from it to see if the next three letters are MAS
                        if check_xmas(lines, i, j, i_dir, j_dir):
                            countP1 += 1

    print(f"Part 1: {countP1}")

    countP2 = 0
    for i,line in enumerate(lines):
        for j,el in enumerate(line):
            if el == 'A':
                if i >= 1 and i < len(lines)-1 and j >=1 and j < len(line)-1:
                    # Given that this element is A, check the two diagonals formed and see if they are MAS
                    diag1 = f'{lines[i-1][j-1]}A{lines[i+1][j+1]}'
                    diag2 = f'{lines[i+1][j-1]}A{lines[i-1][j+1]}'

                    if diag1 in ['SAM', 'MAS'] and diag2 in ['SAM', 'MAS']:
                        countP2 += 1

    print(f"Part 2: {countP2}")