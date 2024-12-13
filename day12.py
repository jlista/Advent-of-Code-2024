with open("C:/Python/2024/day12input.txt", 'r') as file: 

    class Region:
        plots = []
        letter = None

        def __init__(self, plots, letter):
            self.plots = plots
            self.letter = letter
    
    # Parse input
    lines = [list(line.strip()) for line in file]

    HEIGHT = len(lines)
    WIDTH = len(lines[0])

    # detects contiguous groups of plots with the same letter
    def flood_fill(loc, letter, plots, visited):
        global lines
        curY = loc[0]
        curX = loc[1]
        if curY in range(0,HEIGHT) and curX in range(0,WIDTH) and \
        lines[curY][curX] == letter and not visited[curY][curX]:
            
            visited[curY][curX] = True
            plots.append((curY,curX))
     
            flood_fill((curY-1, curX),letter,plots,visited)
            flood_fill((curY+1, curX),letter,plots,visited)
            flood_fill((curY, curX-1),letter,plots,visited)
            flood_fill((curY, curX+1),letter,plots,visited)
            
        return plots

    # run flood fill to detect all regions
    regions = []
    # keep track of which regions have been detected already to avoid duplicates
    visited = [[False for a in line] for line in lines]
    for  y,line in enumerate(lines):
        for x,el in enumerate(line):
            if not visited[y][x]:
                letter = lines[y][x]
                plots = flood_fill((y,x),el,[],visited)
                regions.append(Region(plots, letter))
 
    # Part 1: for each block, determine the perimeter and area
    sumP1 = 0
    for region in regions:
        perimeter = 0
        area = len(region.plots)

        # for each plot around the edge, the perimeter is 4 minus the number of plots it is touching
        for y,x in region.plots:
            
            # get the adjacencies
            up = (y-1, x)
            left = (y, x-1)
            right = (y, x+1)
            down = (y+1, x)

            # check each adjacent plot. It it's not connected (not part of the same region) then add one to the perimeter
            unconnected = 0
            for adj in [up,left,right,down]:
                if adj not in region.plots:
                    unconnected += 1
            perimeter += unconnected
        sumP1 += perimeter * area
    print(f"Part 1: {sumP1}")

    # Part 2: for each plot, determine the number of corners (the number of edges = the number of corners)
    sumP2 = 0
    for region in regions:
        regionCorners = 0
        area = len(region.plots)

        for y,x in region.plots:

            # get the adjacencies (diagonals and the two sides adjacent to the diagonal)
            up = (y-1, x)
            left = (y, x-1)
            right = (y, x+1)
            down = (y+1, x)
            upleft = (y-1, x-1)
            upright = (y-1, x+1)
            downleft = (y+1, x-1)
            downright = (y+1, x+1)

            adjacencies = {
                "upleft": (upleft, up, left),
                "upright": (upright, up, right),
                "downleft": (downleft, down, left),
                "downright": (downright, down, right)
            }

            plotCorners = 0
            # A corner is present if either:
            # A. both adjacent sides are not in the region
            # B. diagonal is not in the region, and both adjacent sides are in the region
            for corner_key in adjacencies:
                corner = adjacencies[corner_key]
                if (corner[1] not in region.plots and corner[2] not in region.plots) or\
                   (corner[0] not in region.plots and corner[1] in region.plots and corner[2] in region.plots):
                    plotCorners += 1

            regionCorners += plotCorners
        sumP2 += regionCorners * area
    print(f"Part 2: {sumP2}")