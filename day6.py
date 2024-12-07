from library import *

with open("C:/Python/2024/day6input.txt", 'r') as file:

    # Parse input 

    lines = [list(line.strip()) for line in file]
    height = len(lines)
    width = len(lines[0])

    visited = []
    for i in range(height):
        visited.append([0]*width)

    for i,line in enumerate(lines):
        for j,el in enumerate(line):
            if el == '^':
                ystart = i
                xstart = j

    # direction will be represented by 0 for up, 1 for right, 2 for down, 3 for left
    dir = 0

    visited[ystart][xstart] = 1
    x = xstart
    y = ystart

    # PART 1
    while True:

        # if we reach the edge, the path ends
        if y == 0 or x == 0 or y == height-1 or x == width-1:
            break

        # based on location and direction, determine the next cell we are visiting
        if dir == 0:
            next = (y-1,x)
        if dir == 1:
            next = (y,x+1)
        if dir == 2:
            next = (y+1,x)
        if dir == 3:
            next = (y,x-1)

        # if we hit an object, turn
        if lines[next[0]][next[1]] == '#':
            dir = (dir + 1) % 4
        # otherwise, move to the next cell
        else:
            y = next[0]
            x = next[1]
            visited[y][x] += 1

    # count the number of cells that were visited
    sumP1 = 0
    for row in visited:
        for cell in row:
            if cell > 0:
                sumP1 += 1

    print(f"Part 1: {sumP1}")
        
    # PART 2
    sumP2 = 0
    for i in range(height):
        for j in range(width):

            # try putting an object in this space. If there already is one, skip it
            if lines[i][j] != '#':
                lines[i][j] = '#'
            else:
                continue
            
            # reset data and counters
            visited = []
            for k in range(height):
                visited.append([0]*width)

            visited[ystart][xstart] = 1
            y = ystart
            x = xstart

            dir = 0
            max_visits = 0      
            while True:
                # if we reach the edge, the path ends
                if y == 0 or x == 0 or y == height-1 or x == width-1:
                    break

                # based on location and direction, determine the next cell we are visiting
                if dir == 0:
                    next = (y-1,x)
                if dir == 1:
                    next = (y,x+1)
                if dir == 2:
                    next = (y+1,x)
                if dir == 3:
                    next = (y,x-1)

                # if we hit an object, turn
                if lines[next[0]][next[1]] == '#':
                    dir = dir + 1
                    if dir == 5:
                        dir = 0
                # otherwise, move to the next cell
                else:
                    y = next[0]
                    x = next[1]
                    visited[y][x] += 1

                    if visited[y][x] > max_visits:
                        max_visits = visited[y][x]

                    if max_visits > 4:
                        # the maximum number of times any cell can be visited without entailing a cycle is 4
                        # (vertical and horizontal * two directions) so if a cell is visited more than 4 times,
                        # we must be in a cycle
                        sumP2 += 1
                        break

            # end simulation, remove the object we added
            lines[i][j] = '.'


    print(sumP2)