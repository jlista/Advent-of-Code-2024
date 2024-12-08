def try_op(cur, nums, index, op, goal):
    # Recurse through the list of numbers, trying each possible operation at each number

    if index == len(nums):
        if cur == goal:
            return True
        return False

    # This is for day 2. Day 1 is the same, just remove the lines with the | operation
    if index == 0:
        val = nums[0]
    elif op == "*":
        val = cur * nums[index]
    elif op == '+':
        val = cur + nums[index]
    elif op == "|":
        val = int(f"{cur}{nums[index]}")

    return try_op(val, nums, index+1, "+", goal) or \
           try_op(val, nums, index+1, "*", goal) or \
           try_op(val, nums, index+1, "|", goal)
    

with open("C:/Python/2024/day7input.txt", 'r') as file:

    # Parse input 

    lines = [line.strip().split(': ') for line in file]
    results = [int(line[0]) for line in lines]
    numlist = [[int(n) for n in line[1].split(' ')] for line in lines]

    count = 0
    for res, nums in zip(results, numlist):
        valid = try_op(0, nums, 0, None, res)
        if valid:
            count += res

    print(count)

