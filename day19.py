

with open("C:/Python/2024/day19input.txt", 'r') as file:

    # Parse input 
    lines = [line.strip() for line in file]
    towels = lines[0].split(", ")
    designs = lines[2:]
 
    num_possible = 0
    sum = 0
    for design in designs:
        dp = [0] * (len(design) + 1)
        for sublen in range(len(design) + 1):
            ways_to_make = 0
            subdesign = design[0:sublen]
            for towel in towels:   
                if subdesign == towel:
                    ways_to_make += 1
                elif subdesign.endswith(towel):
                    ways_to_make += dp[len(subdesign) - len(towel)]
            dp[sublen] = ways_to_make
        if dp[-1] > 0:
            num_possible += 1
        sum += dp[-1]

    print(f"Part 1: {num_possible}")
    print(f"Part 2: {sum}")


