import math
with open("C:/Python/2024/day17input.txt", 'r') as file:

    # Parse input 
    lines = [line.strip() for line in file]
    reg_a = int(lines[0][12:])
    reg_b = int(lines[1][12:])
    reg_c = int(lines[2][12:])

    program = lines[4][9:]
    program = [int(n) for n in program.split(",")]

    def get_combo(operand):
        # handle the combo operands as described in the problem
        if operand <= 3:
            return operand
        if operand == 4:
            return reg_a
        if operand == 5:
            return reg_b
        if operand == 6:
            return reg_c
        
    def simulate(new_a):
        # run the program
        global reg_a,reg_b,reg_c
        pointer = 0
        reg_a = new_a
        outputs = []
        while True:

            if pointer not in range(len(program)):
                break
            opcode = program[pointer]
            operand = program[pointer+1]

            if opcode == 0:
                operand = get_combo(operand)
                reg_a = int(math.floor(reg_a / (2 ** operand)))
            elif opcode == 1:
                reg_b = reg_b ^ operand
            elif opcode == 2:
                operand = get_combo(operand)
                reg_b = operand % 8
            elif opcode == 3:
                if int(reg_a) != 0:
                    pointer = operand
                    continue
            elif opcode == 4:
                reg_b = reg_c ^ reg_b
            elif opcode == 5:
                operand = get_combo(operand)
                outputs.append(operand % 8)
            elif opcode == 6:
                operand = get_combo(operand)
                reg_b = int(math.floor(reg_a / (2 ** operand)))
            elif opcode == 7:
                operand = get_combo(operand)
                reg_c = int(math.floor(reg_a / (2 ** operand)))

            pointer += 2

        return outputs

    def get_lowest_value_for_digit(digit,target,lower_bound,upper_bound,skip):
        # this is a binary search method to find the lowest reg_a value that will produce a given number (target)
        # at a given output position (digit)
   
        num_iterations = 0
        for n in range(lower_bound,upper_bound,skip):
            output = simulate(n)
            if len(output) == 16 and output[digit] == target:
                new_lower_bound = int(lower_bound + (num_iterations-1)*skip)
                new_upper_bound = int(8*lower_bound)
                new_skip = int(skip/8)
                if skip == 1:
                    return n
                return get_lowest_value_for_digit(digit,target,new_lower_bound,new_upper_bound,new_skip)
            num_iterations += 1

    def converge(digit,lower_bound,upper_bound,skip):
        # it turns out that as the starting value of reg_a increases, the last output digit changes the slowest,
        # the second-to-last changes about 8x faster, and so on. This means we can start by finding the lowest 
        # input that will produce 0 in the last position, then use intervals 1/8th the size to search for the
        # lowest input that will produce 3 in the second-to-last position and keep recursing until we've found
        # all of the digits.
        global program
        if digit < 0:
            return lower_bound
        target = program[digit]
        val = get_lowest_value_for_digit(digit,target,lower_bound,upper_bound,skip)
        return converge(digit-1, val, 8*val, int(skip/8))

    part1 = (",".join([str(o) for o in simulate(reg_a)]))
    print(f"Part 1: {part1}")
    part2 = converge(15,8**15,8**16,8**15)
    print(f"Part 2: {part2}")