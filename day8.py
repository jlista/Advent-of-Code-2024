import itertools

# Note: this solution is a complete mess and has some serious logical oversights. I'm just leaving it as is
# because that's what I came up with at the time

with open("C:/Python/2024/day8input.txt", 'r') as file:

    # Parse input 

    nodes = {}

    lines = [list(line.strip()) for line in file]

    antinodes = [['.']*len(lines[0]) for l in lines] 

    for i, line in enumerate(lines):
        for j, el in enumerate(line):
            if el != '.':
                if el not in nodes.keys():
                    nodes[el] = [(i,j)]
                else:
                    nodes[el].append((i,j))

    for freq in nodes.keys():
        # for each pair, figure out the two antinodes it forms
        pairs = list(itertools.product(nodes[freq], repeat=2))

        for pair in pairs:
            node1 = pair[0]
            node2 = pair[1]
            if pair[0] != pair[1]:
                ydif = abs(pair[0][0] - pair[1][0])
                xdif = abs(pair[0][1] - pair[1][1])

                if node1[0] > node2[0]:
                    antiy1 = node1[0] + ydif
                    antiy2 = node2[0] - ydif
                else:
                    antiy1 = node1[0] - ydif
                    antiy2 = node2[0] + ydif

                if node1[1] > node2[1]:
                    antix1 = node1[1] + xdif
                    antix2 = node2[1] - xdif
                else:
                    antix1 = node1[1] - xdif
                    antix2 = node2[1] + xdif
                
                anti1 = (antiy1, antix1)
                anti2 = (antiy2, antix2)
                if antiy1 >= 0 and antix1 >= 0 and antiy1 < len(lines) and antix1 < len(lines[0]):
                    antinodes[antiy1][antix1] = '#'
                if antiy2 >= 0 and antix2 >= 0 and antiy2 < len(lines) and antix2 < len(lines[0]):
                    antinodes[antiy2][antix2] = '#'
    sum = 0
    for row in antinodes:
        for el in row:
            if el == '#':
                sum += 1
    print(f"Part 1: {sum}")



    antinodes = [['.']*len(lines[0]) for l in lines] 

    for freq in nodes.keys():
        pairs = list(itertools.product(nodes[freq], repeat=2))

        for pair in pairs:
            node1 = pair[0]
            node2 = pair[1]
            if pair[0] != pair[1]:
                ydif = abs(pair[0][0] - pair[1][0])
                xdif = abs(pair[0][1] - pair[1][1])


                if node1[0] > node2[0]:
                    temp = node1
                    node1 = node2
                    node2 = temp # make sure node 1 is at the top


                if node1[1] > node2[1]: # if top right to bottom left
                    antiy = node1[0]
                    antix = node1[1]
                    while antiy >= 0 and antix >= 0 and antiy < len(lines) and antix < len(lines[0]):
                        # diagonal up
                        antinodes[antiy][antix] = '#'
                        antiy -= ydif
                        antix += xdif
                    antiy = node1[0]
                    antix = node1[1]
                    while antiy >= 0 and antix >= 0 and antiy < len(lines) and antix < len(lines[0]):
                        # diagonal down
                        antinodes[antiy][antix] = '#'
                        antiy += ydif
                        antix -= xdif

                else: # if top left to bottom right
                    antiy = node1[0]
                    antix = node1[1]
                    while antiy >= 0 and antix >= 0 and antiy < len(lines) and antix < len(lines[0]):
                        # diagonal up

                        antinodes[antiy][antix] = '#'
                        antiy -= ydif
                        antix -= xdif
                    antiy = node1[0]
                    antix = node1[1]
                    while antiy >= 0 and antix >= 0 and antiy < len(lines) and antix < len(lines[0]):
                        # diagonal down
                        antinodes[antiy][antix] = '#'
                        antiy += ydif
                        antix += xdif
    sum = 0
    for row in antinodes:
        for el in row:
            if el == '#':
                sum += 1
    print(f"Part 2: {sum}")
