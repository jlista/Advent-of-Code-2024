import re

with open("C:/Python/2024/day3input.txt", 'r') as file:

    lines = [line.strip() for line in file]
    # combine all input lines into one big line
    bigline = "".join(lines)

    # Part 1: extract all product instructions
    products = re.findall(r"mul\(\d{1,3},\d{1,3}\)", bigline)

    # multiply and add the numbers up
    valP1 = 0
    for prod in products:
        spl = prod[4:-1].split(',')
        valP1 += int(spl[0]) * int(spl[1])

    print(f"Part 1: {valP1}")

    # Part 2: extract all products, dos and don'ts
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", bigline)

    # use the do and don't instructions to control the do flag. Multiply and add numbers only if do = True
    valP2 = 0
    do = True
    for instruction in matches:
        if instruction == 'don\'t()':
            do = False
        elif instruction == 'do()':
            do = True
        elif do:
            spl = instruction[4:-1].split(',')
            valP2 += int(spl[0]) * int(spl[1])

    print(f"Part 2: {valP2}")