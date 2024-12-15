
import math

class Prize:
    ax=0
    ay=0
    bx=0
    by=0
    xloc=0
    yloc=0
    def __init__(self, ax,ay,bx,by,xloc,yloc):
        self.ax=ax 
        self.ay=ay
        self.bx=bx
        self.by=by
        # add  10000000000000 for part 2, leave out for part 1
        self.xloc=xloc + 10000000000000
        self.yloc=yloc + 10000000000000

def split_list(l, sep):
    """
    given a list and a separator, return sublists
    """
    lists = []
    i = 0
    segment_start = 0
    while i < len(l):
        if l[i] == sep:
            lists.append(l[segment_start:i])
            segment_start = i+1
        i += 1
    
    return lists

with open("C:/Python/2024/day13input.txt", 'r') as file: 

    # Parse input
    lines = [line.strip() for line in file]
    prizestxt = split_list(lines, "")

    prizes = []
    for prize in prizestxt:
        ax = int(prize[0][12:14])
        ay = int(prize[0][18:20])
        bx = int(prize[1][12:14])
        by = int(prize[1][18:20])
        locs = prize[2].split(',')
        xloc = int(locs[0][9:])
        yloc = int(locs[1][3:])
        prizes.append(Prize(ax,ay,bx,by,xloc,yloc))

    sum = 0
    for prize in prizes:

        # System of equations:
        # a*ax + b*bx = xloc
        # a*ay + b*by = yloc
        # the equations for a and b come from solving this system via elimination

        b_numerator = int(prize.xloc * prize.ay - prize.yloc * prize.ax)
        b_denominator = int(prize.bx*prize.ay - prize.by*prize.ax)

        # if the GCD of the numerator and denominator = the smaller of the two, the result will be an integer
        if math.gcd(b_numerator, b_denominator) == min(abs(b_numerator), abs(b_denominator)):
            b = int(b_numerator / b_denominator)
            a_numerator = int(prize.xloc - b*prize.bx)
            a_denominator = int(prize.ax)
            if math.gcd(a_numerator, a_denominator) == min (abs(a_numerator), abs(a_denominator)):
                # if a and b are both integers, it's possible to win a prize
                a = int(a_numerator / a_denominator)
                val = 3*a + b
                sum += val
    print(sum)

