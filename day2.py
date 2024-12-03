
import copy

def check_line(line):
    # checks if a line is safe (all differences between subsequent elements are <=3 and all have the same sign)
    diffs = []
    for i in range(0, len(line)-1):
        diffs.append(line[i+1] - line[i])

    for diff in diffs:
         if abs(diff) > 3:
              return False
         if diff * diffs[0] <= 0: # this makes sure all differences have the same sign (pos*pos=pos, neg*neg=pos, pos*neg=neg)
              return False
    return True

with open("C:/Python/2024/day2input.txt", 'r') as file:

    lines = [line.strip() for line in file]
    lines = [[int(n) for n in line.split(" ")] for line in lines]

    numsafeP1 = 0
    for line in lines:
        if check_line(line):
             numsafeP1 += 1

    print(f"part 1: {numsafeP1}")

    # for each line, generate all possible lines that have one of the elements removed
    numsafeP2 = 0
    for line in lines:
        test_combos = []
        for i in range(len(line)):
            newline = copy.deepcopy(line)
            del newline[i]
            test_combos.append(newline)

        # test each of these new lines
        checks = [check_line(ln) for ln in test_combos]
        if check_line(line) or checks.count(True) > 0:
            numsafeP2 += 1

    print(f"part 2: {numsafeP2}")
    