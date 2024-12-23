import heapq
import sys

with open("C:/Python/2024/day20input.txt", 'r') as file:

    MAX_CHEAT = 20 # 2 for part 1, 20 for part 2

    # Parse input, get dimensions and starting/ending positions
    racetrack = [list(line.strip()) for line in file]

    height = len(racetrack)
    width = len(racetrack[1])

    for y,line in enumerate(racetrack):
        for x,el in enumerate(line):
            if el == "S":
                start_x = x
                start_y = y
            if el == "E":
                end_x = x
                end_y = y

    # traverse the path to find all vertices on the path
    path = []
    def find_path(y,x,path):
        while True:
            path.append((y,x))

            if (y,x) == (end_y,end_x):
                return path
            
            neighbor_coords = [(1,0),(0,1),(-1,0),(0,-1)]
            for coords in neighbor_coords:
                ny = coords[0] + y
                nx = coords[1] + x
                if (ny,nx) not in path and racetrack[ny][nx] != "#":
                    path
                    y = ny
                    x = nx
                    break
    path = find_path(start_y,start_x,[])

    # find all possible cheats
    time_savings = {}
    # check each combination of two vertices
    for i,(y1,x1) in enumerate(path):   
        for j,(y2,x2) in enumerate(path[i+1:]):
            
            # find the number of vertices we have to cheat to get from i to j
            ydiff = abs(y1 - y2)
            xdiff = abs(x1 - x2)
            path_len = ydiff + xdiff

            # this is short enough, calculate the time savings and record it
            if path_len <= MAX_CHEAT:
                time_saved = j - path_len + 1
                if time_saved >= 100:
                    if time_saved not in time_savings.keys():
                        time_savings[time_saved] = 1
                    else:
                        time_savings[time_saved] += 1

    num_cheats = 0
    for amt in time_savings.keys():
        num_cheats += time_savings[amt]
    print(num_cheats)