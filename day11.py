with open("C:/Python/2024/day11input.txt", 'r') as file:

    # Parse input 

    lines = [line for line in file]
    stones = [int(n) for n in lines[0].split(" ")]

    # create map of stones values to the number of times that stone appears
    stoneMap = {}
    def insert(smap, stone, count):
        if stone not in smap.keys():
            smap[stone] = count
        else:
            smap[stone] += count

    for stone in stones:
        insert(stoneMap,stone,1)

    def blink():
        # For each iteration, determine the result of each stone and store the results in the map
        global stoneMap
    
        newmap = {}
        for stone in stoneMap.keys():
            stone_str = f"{stone}"
            num_digits = len(stone_str)

            count = stoneMap[stone]
            if stone == 0:
                insert(newmap,1,count)
            elif num_digits % 2 == 0:
                insert(newmap,int(stone_str[0:num_digits//2]),count)
                insert(newmap,int(stone_str[num_digits//2:]),count)
            else:
                insert(newmap,stone*2024,count) 
        stoneMap = newmap
        
    for i in range(75):
        blink()

    print(sum(stoneMap.values()))