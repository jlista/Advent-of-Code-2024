import sys

with open("C:/Python/2024/day9input.txt", 'r') as file:

    # Parse input 

    nodes = {}

    lines = [list(line.strip()) for line in file]
    line = [int(l) for l in  lines[0]]

    blocks = []
    gaps = []
    diskmap = []

    # Get list of blocks, gaps, and the expanded map showing every memory space
    for i,el in enumerate(line):
        if i%2 == 0:
            blocks.append(el)
            val = int(i/2)
            diskmap.extend([val]*el)
        else:
            gaps.append(el)
            diskmap.extend(['.']*el)

    # Part 1

    gap_index = 0
    current_gap_start = blocks[gap_index]
    current_gap_size = gaps[gap_index]

    # iterate through the map backwards, keeping track of the earliest available gap and moving any element
    # into that gap
    for i in range (len(diskmap) - 1, 0, -1):

        el = diskmap[i]

        if el != '.':

            # if we have filled up a gap, move on to the next nonzero gap
            if current_gap_size == 0:
                gap_index += 1

                while gaps[gap_index] == 0:
                    gap_index += 1

                current_gap_start = sum(gaps[0:gap_index]) + sum(blocks[0:gap_index+1])
                current_gap_size = gaps[gap_index]

            if current_gap_start >= i:
                # ending condition
                break

            diskmap[current_gap_start] = el
            diskmap[i] = '.'
            current_gap_start += 1
            current_gap_size -= 1
    
    checksumP1 = 0
    for i,el in enumerate(diskmap):
        if el != '.':
            checksumP1 += el * i

    print(f"Part 1: {checksumP1}")
    
    # PART 2

    # Re-initialize diskmap
    diskmap = []
    for i,el in enumerate(line):
        if i%2 == 0:
            val = int(i/2)
            diskmap.extend([val]*el)
        else:
            diskmap.extend(['.']*el)

    # calculate the index where each memory block starts
    block_starts = []
    for index in range(len(blocks)):
        block_starts.append(sum(blocks[0:index]) + sum(gaps[0:index]))

    # calculate the index where each gap starts, sorted by the size of the gap
    gap_starts_by_size = [[] for i in range(10)]
    for i, gap_len in enumerate(gaps):
        gap_start = sum(gaps[0:i]) + sum(blocks[0:i+1])
        gap_starts_by_size[gap_len].append(gap_start)

    # iterate through the list of blocks backwards and attempt to move each block into a gap
    for block_index in range(len(blocks)-1, 0, -1):
        block_len = blocks[block_index]
        block_start = block_starts[block_index]

        # Find the earliest gap that is large enough to fit the block, if there is one
        gap_start = sys.maxsize
        original_gap_size = 0
        for j,gaplist in enumerate(gap_starts_by_size):
            if j >= block_len and len(gaplist) >0 and gaplist[0] < block_start and gaplist[0] < gap_start:
                gap_start = gaplist[0]
                original_gap_size = j
        
        # If we did not find a suitable gap, skip this block and move on to the next
        if gap_start == sys.maxsize:
            continue
        
        # Move the memory block into the gap
        for i in range(gap_start, gap_start + block_len):
            diskmap[i] = block_index
        for i in range(block_start, block_start + block_len):
            diskmap[i] = '.'

        # Since the gap has been shrunken, find its new size and location
        new_gap_size = original_gap_size - block_len
        new_gap_start = gap_start + block_len
        
        # Remove the gap from its original place in the gap list and put it in the new proper location
        gap_starts_by_size[original_gap_size] = gap_starts_by_size[original_gap_size][1:]
        inserted = False
        for k,smallgap in enumerate(gap_starts_by_size[new_gap_size]):
            if smallgap > new_gap_start:
                gap_starts_by_size[new_gap_size].insert(k,new_gap_start)
                inserted = True
                break
        if not inserted:
            gap_starts_by_size[new_gap_size].append(smallgap)
        
    checksumP2 = 0
    for i,el in enumerate(diskmap):
        if el != '.':
            checksumP2 += el * i

    print(f"Part 2: {checksumP2}")
