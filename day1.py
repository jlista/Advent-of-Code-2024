def get_col(l, x):
    col = []
    for row in l:
        col.append(row[x])
    return col

def get_cols(l):
    cols = []
    for x in range(0, len(l[0])):
        cols.append(get_col(l, x))
    return cols

with open("C:/Python/2024/day1input.txt", 'r') as file:

    # parse input
    lines = [line.strip() for line in file]
    nums = [[int(a) for a in line.split('   ')] for line in lines]
    cols = get_cols(nums)

    c1 = sorted(cols[0])
    c2 = sorted(cols[1])

    sum1 = 0
    for (p1, p2) in zip(c1, c2):
        sum1 += abs(p1-p2)

    print(f"Part 1: {sum1}")

    sum2 = 0
    for p1 in c1:
        occs = c2.count(p1)
        sum2 += p1*occs

    print(f"Part 2: {sum2}")