import math

WIDTH = 101
HEIGHT = 103
    
class Robot:
    px = 0
    py = 0
    vx = 0
    vy = 0
    def __init__(self,px,py,vx,vy):
        self.px=px
        self.py=py
        self.vx=vx
        self.vy=vy

    def simulate(self,n):
        # find the position of the robot after n seconds

        dx = n*self.vx
        dy = n*self.vy

        self.px = (self.px + dx) % WIDTH
        self.py = (self.py + dy) % HEIGHT

    def quadrant(self):
        # find which quadrant the robot is in. If it's in the center, return 0.
        if self.px < WIDTH//2:
            if self.py < HEIGHT//2:
                return 1
            if self.py > HEIGHT//2:
                return 2
        if self.px > WIDTH//2:
            if self.py < HEIGHT//2:
                return 3
            if self.py > HEIGHT//2:
                return 4
        return 0 

with open("C:/Python/2024/day14input.txt", 'r') as file: 
 
    # Parse input
    lines = [line.strip() for line in file]

    robots = []
    for line in lines:
        spl = line.split(" ")
        pos = spl[0][2:]
        vel = spl[1][2:]
        pos = pos.split(",")
        vel = vel.split(",")
        px = int(pos[0])
        py = int(pos[1])
        vx = int(vel[0])
        vy = int(vel[1])
        robots.append(Robot(px,py,vx,vy))
    
    # Part 1
    quadrants = [0,0,0,0,0]
    for robot in robots:
        robot.simulate(100)
        quadrants[robot.quadrant()] += 1
    safety_factor = math.prod(quadrants[1:])
    print(f"Part 1: {safety_factor}")

    # part 2
    max_in_center = 0
    # note that we already did the first 100 iterations in part 1 so we can start at the 101st for part 2
    for n in range(101,10000):
        quadrants = [0,0,0,0,0]
        for robot in robots:
            robot.simulate(1)
            quadrants[robot.quadrant()] += 1

        # the tree is mostly on one side, so we're looking for states with a large difference between the number of
        # robots on each side. The number 317 comes from checking a large number of states and seeing what the highest
        # numbers tend to be. This fill filter out most states, making it easy to find the tree through visual inspection.
        if (abs((quadrants[1]+quadrants[2]) - (quadrants[3] + quadrants[4]))) > 317:    

            # build up a grid object showing the number of robots in each space and print it
            grid = []
            for i in range(HEIGHT):
                grid.append([])
                for j in range(WIDTH):
                    grid[i].append(0)

            for robot in robots:
                grid[robot.py][robot.px] += 1

            print(f"{n}\n")
            for line in grid:
                display = ""
                for el in line:
                    if el == 0:
                        display += "."
                    else:
                        display += f"{el}"
                print(f"{display}\n")
