def calculate_move(move):
    if move == '^':
        return -1,0
    if move  == '>':
        return 0,1
    if move == 'v':
        return 1,0
    if move == '<':
        return 0,-1

with open("C:/Python/2024/day15input.txt", 'r') as file:

    # Parse input 
    lines = [line.strip() for line in file]

    spl_index = lines.index("")
    gridtxt = lines[0:spl_index]
    moves = list(''.join(lines[spl_index+1:]))

    grid = []
    for line in gridtxt:
        grid.append(list(line))

    height = len(grid)
    width = len(grid[0])

    # find the starting point and set initial x,y values
    curY = 0
    curX = 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] == '@':
                curY = i
                curX = j
                break

    # Part 1: simulate all moves
    for move in moves:
        dy,dx = calculate_move(move)
        destY = curY + dy
        destX = curX + dx
        if grid[destY][destX] != '#':
            if grid[destY][destX] == '.':
                grid[curY][curX] = '.'
                grid[destY][destX] = '@'
                curY = destY
                curX = destX
            if grid[destY][destX] == 'O':
                next_spot = grid[destY][destX]
                num_boxes = 0
                while next_spot == 'O':
                    num_boxes += 1
                    next_spot = grid[destY + num_boxes*dy][destX + num_boxes*dx]
                if next_spot == '.':
                    grid[curY][curX] = '.'
                    grid[destY][destX] = '@'
                    for i in range(1,num_boxes+1):
                        grid[destY + i*dy][destX + i*dx] = 'O'
                    curY = destY
                    curX = destX

    sum = 0
    for y,line in enumerate(grid):
        for x,el in enumerate(line):
            if el == 'O':
                sum += 100*y + x

    print(f"Part 1: {sum}")
    
    # re-initialize the grid for part 2
    grid = []
    for line in gridtxt:
        grid.append(list(line))

    height = len(grid)
    width = len(grid[0])

    # convert the grid into a widened grid
    
    wide_grid = []
    for line in gridtxt:
        wide_grid.append([None]*2*width)
    for i in range(height):
        for j in range(width):
            if grid[i][j] == '#':
                wide_grid[i][2*j] = '#'
                wide_grid[i][2*j+1] = '#'
            if grid[i][j] == '.':
                wide_grid[i][2*j] = '.'
                wide_grid[i][2*j+1] = '.'
            if grid[i][j] == '@':
                wide_grid[i][2*j] = '@'
                wide_grid[i][2*j+1] = '.'
                curY = i
                curX = 2*j    
            if grid[i][j] == 'O':
                wide_grid[i][2*j] = '['
                wide_grid[i][2*j+1] = ']'         

    # find the new starting position
    curY = 0
    curX = 0
    for i in range(height):
        for j in range(width*2):
            if wide_grid[i][j] == '@':
                curY = i
                curX = j
                break

    for move in moves:

        dy,dx = calculate_move(move)
        destY = curY + dy
        destX = curX + dx

        if destY in range(0, height) and destX in range(0, width*2) and wide_grid[destY][destX] != '#':
            if wide_grid[destY][destX] == '.':
                wide_grid[curY][curX] = '.'
                wide_grid[destY][destX] = '@'
                curY = destY
                curX = destX
            a = wide_grid[destY][destX]
            if wide_grid[destY][destX] in ['[',']']:

                # Handle the case where boxes are pushed horizontally
                # this works just like part 1
                if move in ['<','>']:
                    next_spot = wide_grid[destY][destX]
                    num_boxes = 0
                    while next_spot in ['[',']']:
                        num_boxes += 1
                        next_spot = wide_grid[destY + num_boxes*dy][destX + num_boxes*dx]
                    if next_spot == '.':
                        wide_grid[curY][curX] = '.'
                        wide_grid[destY][destX] = '@'
                        for i in range(1,num_boxes+1, 2):
                            wide_grid[destY + i*dy][destX + i*dx] = '[' if move == '>' else ']'
                            wide_grid[destY + i*dy][destX + (i+1)*dx] = ']' if move == '>' else '['
                        curY = destY
                        curX = destX
                else:
                    # handle the case were boxes are pushed vertically
                    stuck = False

                    # keep track of the indices of all boxes we need to move, also including the robot itself
                    indices_to_move = {(curY,curX)}

                    # starting at the robot's position, check each row until we either hit a wall or the row contains no more boxes to push
                    row_to_check = destY
                    while not stuck:
                        next_row_clear = True
                
                        # for this row, check each element to see if it's a wall or box
                        for x,el in enumerate(wide_grid[row_to_check]):
                            # if it's a wall and it is in front of a moving box, we are stuck
                            if el == "#" and (row_to_check-dy,x) in indices_to_move:
                                stuck = True
                                next_row_clear = False
                            # if it's a box, check if it's in front of a moving box
                            if el == '[':
                                if (row_to_check-dy,x) in indices_to_move \
                                or (row_to_check-dy,x+1) in indices_to_move:  # also check the space directly to the side, since the boxes might not overlap perfectly
                                    # if this box is in front of a moving box, add it to the list of moving boxes
                                    indices_to_move.add((row_to_check,x))
                                    next_row_clear = False
                            if el == ']':
                                if (row_to_check-dy,x) in indices_to_move \
                                or (row_to_check-dy,x-1) in indices_to_move:
                                    indices_to_move.add((row_to_check,x))
                                    next_row_clear = False
                        if next_row_clear:
                            # if we did not find any boxes or walls in this row, stop searching and continue on to move them
                            break
                        else:
                            # otherwise, check the next row
                            row_to_check += dy

                    if not stuck:
                        new_box_indices = set()
                        # fill in the spaces where the boxes used to be with dots, and store a set of their new locations
                        for (ybox, xbox) in indices_to_move:
                            symbol = wide_grid[ybox][xbox]
                            new_box_indices.add((ybox+dy, xbox, symbol))
                            wide_grid[ybox][xbox] = '.'
                        # put the boxes in their new locations
                        for (ybox, xbox, symbol) in new_box_indices:
                            wide_grid[ybox][xbox] = symbol
                        curY = destY
                        curX = destX

    sum = 0
    for y,line in enumerate(wide_grid):
        for x,el in enumerate(line):
            if el == '[':
                sum += 100*y + x

    print(f"Part 2: {sum}")






   