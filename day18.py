import sys
import heapq

SIZE = 71
NUM_BYTES = 1024

sys.setrecursionlimit(5000)
class Node(object):
    def __init__(self, x,y,cost):
        self.x=x
        self.y=y
        self.cost=cost
        self.visited=False
        self.prev=None

    def __lt__(self, other):
        return self.cost < other.cost

with open("C:/Python/2024/day18input.txt", 'r') as file:

    # Parse input 
    lines = [line.strip() for line in file]
    coordinates = [[int(a) for a in b.split(",")] for b in lines]

    def get_shortest_path(num_bytes):
        # Dijkstra's algorithm

        # Initialize the nodes and unvisited list
        nodes = {}
        for x in range(SIZE):
            nodes[x] = [None]*SIZE
            for y in range(SIZE):
                cost = sys.maxsize
                if x==0 and y==0: 
                    cost = 0
                
                nodes[x][y] = Node(x,y,cost)

        unvisited = [nodes[0][0]]
        heapq.heapify(unvisited)
        while True:
            current_node = heapq.heappop(unvisited)
            
            for direction in [(-1,0),(1,0),(0,1),(0,-1)]:
                neighbor_coord = (current_node.x + direction[0], current_node.y + direction[1])
                if neighbor_coord[0] in range(SIZE) and neighbor_coord[1] in range(SIZE):
                    neighbor = nodes[neighbor_coord[0]][neighbor_coord[1]]
                    if  not neighbor.visited and [neighbor.x,neighbor.y] not in coordinates[0:num_bytes]:
                
                            newcost = current_node.cost + 1
                            if newcost < neighbor.cost:
                                neighbor.cost = newcost
                                neighbor.prev = [current_node.x,current_node.y]
                            if neighbor not in unvisited:
                                heapq.heappush(unvisited,neighbor)
            current_node.visited = True
            if len(unvisited) == 0:
                break
        # reconstruct and return the shortest path
        path = []
        def traverse(x,y):
            node = nodes[x][y]
            if node.prev == None:
                return
            path.append([x,y])
            traverse(node.prev[0],node.prev[1])
        traverse(SIZE-1,SIZE-1)

        return path

    part1 = get_shortest_path(NUM_BYTES)
    print(f"Part 1: {len(part1)}")

    # Part 2
    num_bytes = NUM_BYTES
    while True:
        shortest_path = get_shortest_path(num_bytes)
        if len(shortest_path) == 0:
            print(f"Part 2: {num_bytes}, {coordinates[num_bytes-1]}") 
            break
        else:
            # if we have a known path, drop bytes until one blocks the path
            # then return to the outer loop to try to find a new path
            # keep doing this until no more paths can be found
            blocked = False
            while not blocked:
                num_bytes += 1
                next_byte = coordinates[num_bytes-1]
                if next_byte in shortest_path:
                    blocked = True
            
