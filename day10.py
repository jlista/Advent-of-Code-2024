with open("C:/Python/2024/day10input.txt", 'r') as file:

    input = [list(line.strip()) for line in file]
    lines = []
    for line in input:
        mapline = [int(el) for el in line]
        lines.append(mapline)
    
    def traverse(y, x, visited, ispart2):
        cur = lines[y][x]
        if cur == 9:
            if ispart2:
                return 1
            else:
                if not visited[y][x]:
                    visited[y][x] = True
                    return 1
                return 0
        
        sum9s = 0
        if y >= 1 and lines[y-1][x] == cur+1:
            sum9s += traverse(y-1,x,visited,ispart2)
        if y < len(lines)-1 and lines[y+1][x] == cur+1:
            sum9s += traverse(y+1,x,visited,ispart2)
        if x >= 1 and lines[y][x-1] == cur+1:
            sum9s += traverse(y,x-1,visited,ispart2)
        if x < len(lines[0])-1 and lines[y][x+1] == cur+1:
            sum9s += traverse(y,x+1,visited,ispart2)
        return sum9s

    sumP1 = 0
    sumP2 = 0
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == 0:
                visited = []
                for line in lines:
                    visited.append([False] * len(line))
                sumP1 += traverse(y,x,visited,False)
                sumP2 += traverse(y,x,None,True)
    print(f"Part 1: {sumP1}")
    print(f"Part 2: {sumP2}")