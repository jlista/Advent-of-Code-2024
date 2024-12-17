import heapq
import sys

class Node(object):
    def __init__(self, y,x,dir,cost,neighbors):
        self.x=x
        self.y=y
        self.dir=dir
        self.cost=cost
        self.neighbors=neighbors
        self.visited=False
        self.prev=set()

    def __lt__(self, other):
        return self.cost < other.cost

with open("C:/Python/2024/day16input.txt", 'r') as file:

    # Parse input 

    maze = [list(line.strip()) for line in file]

    height = len(maze)
    width = len(maze[0])
    # Get the starting and ending points
    for y,line in enumerate(maze):
        for x,el in enumerate(line):
            if el == 'S':
                sx = x
                sy = y
            if el == 'E':
                ex = x
                ey = y

    # Create a node for each combination of x,y,direction
    nodes = {}
    for y,line in enumerate(maze):
        for x,el in enumerate(line):
            if maze[y][x] != "#":
                for dir in range(4):
                    nodes[(y,x,dir)] = Node(y,x,dir,sys.maxsize,[])
                   
    # find the neighbors of each node and store them along with the cost of moving there 
    for (y,x,dir) in nodes.keys():
                   
        adjacencies = [(-1,0),(0,1),(1,0),(0,-1)]
        for i,adj in enumerate(adjacencies):
            destY = y + adj[0]
            destX = x + adj[1]
            if destY in range(height) and destX in range(height) and maze[destY][destX] != '#':
                if dir == i:
                    nodes[(y,x,dir)].neighbors.append([nodes[destY,destX,dir],1])
                elif (dir + 1) % 4 == i or (dir + 3) % 4 == i:
                    nodes[(y,x,dir)].neighbors.append([nodes[destY,destX,i],1001])

    # set the starting node's cost to 0 and initialize the queue with that node
    start_node = nodes[(sy,sx,1)]
    start_node.cost = 0
    unvisited = [start_node]
    heapq.heapify(unvisited)
    
    while True:
        # use Dijkstra's algorithm to find the cheapest path
        current_node = heapq.heappop(unvisited)

        for neighbor,edge_cost in current_node.neighbors:
            neighbor_loc = (neighbor.y,neighbor.x,neighbor.dir)
            if not neighbor.visited:  
                newcost = current_node.cost + edge_cost
                if newcost < neighbor.cost:
                    neighbor.cost = newcost
                    neighbor.prev = set([current_node])
                if newcost == neighbor.cost:
                    neighbor.prev.add(current_node)
                heapq.heappush(unvisited,neighbor)

        current_node.visited = True
        if len(unvisited) == 0:
            break

    # the exit point has 4 possible nodes corresponding to the 4 directions. Find the cheapest one.
    outputs = [nodes[(ey,ex,d)].cost for d in range(4)]
    print(f"Part 1: {min(outputs)}")
    last_dir = outputs.index(min(outputs))

    # Part 2: traverse the path from the exit node to the start node and count how many seats are on the path
    best_seats = set()
    def traverse(node):
        best_seats.add((node.y,node.x))
        if len(node.prev) == 0:
            return
        for prev_node in node.prev:
            traverse(prev_node)

    traverse(nodes[(ey,ex,last_dir)])
    print(f"Part 2: {len(best_seats)}")

    
