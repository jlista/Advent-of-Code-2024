import sys

sys.setrecursionlimit(5000)
with open("C:/Python/2024/day21input.txt", 'r') as file:

    num_keypad = {
        "7": (0,0),
        "8": (0,1),
        "9": (0,2),
        "4": (1,0),
        "5": (1,1),
        "6": (1,2),
        "1": (2,0),
        "2": (2,1),
        "3": (2,2),
        "0": (3,1),
        "A": (3,2)
    }

    dir_keypad = {
        "^": (0,1),
        "A": (0,2),
        "<": (1,0),
        "v": (1,1),
        ">": (1,2)
    }

    # Parse input 
    codes = [line.strip() for line in file]

    def get_directional_instructions(code):
            sequence = ""
        
            curY = 0
            curX = 2
            for c in code:

                dest = dir_keypad[c]
                y_diff = dest[0] - curY
                x_diff = dest[1] - curX

                left_moves = ["<" if x_diff < 0 else None] * abs(x_diff)
                right_moves = [">" if x_diff > 0 else None] * abs(x_diff)
                up_moves = ["^" if y_diff < 0 else None] * abs(y_diff)
                down_moves = ["v" if y_diff > 0 else None] * abs(y_diff)
                # handle cases where it would pass over the empty spot
                if curY == 0 and dest[1] == 0:
                    # forced to do down -> left
                    new_sequence = [m for m in down_moves + left_moves if m is not None]

                elif dest[0] == 0 and curX == 0:
                    # forced to do right -> up
                    new_sequence = [m for m in right_moves + up_moves if m is not None]
                # otherwise, instructions should be in the order left>down>up>right to ensure minimum length
                else:
                    new_sequence = [m for m in left_moves + down_moves + up_moves + right_moves if m is not None]

                sequence += "".join(new_sequence)
                sequence += "A"
                curY = dest[0]
                curX = dest[1]
                
            return sequence

    def get_numerical_instructions(code):
        sequence = ""
        curY = 3
        curX = 2

        for c in code:
            dest = num_keypad[c]
            y_diff = dest[0] - curY
            x_diff = dest[1] - curX

            left_moves = ["<" if x_diff < 0 else None] * abs(x_diff)
            right_moves = [">" if x_diff > 0 else None] * abs(x_diff)
            up_moves = ["^" if y_diff < 0 else None] * abs(y_diff)
            down_moves = ["v" if y_diff > 0 else None] * abs(y_diff)
            if curY == 3 and dest[1] == 0:
                # forced to do up -> left
                new_sequence = [m for m in up_moves + left_moves if m is not None]
            elif dest[0] == 3 and curX == 0:
                # forced to do right -> down
                new_sequence = [m for m in right_moves + down_moves if m is not None]

            else:
                new_sequence = [m for m in left_moves + down_moves + up_moves + right_moves if m is not None]      
            new_sequence = "".join(new_sequence)
            sequence += "".join(new_sequence)
            sequence += "A"
            curY = dest[0]
            curX = dest[1]
        return sequence


# Given a long sequence of commands, split it into smaller parts each ending in A in order to divide and conquer
def split_code_segments(code):
    code_segments = []
    index = 0
    start_index = 0
    found_a = False
    while True:
        if index == len(code):
            code_segments.append(code[start_index:index])
            break
        c = code[index]
        if c == "A":
            found_a = True
        if found_a and c != "A":
            code_segments.append(code[start_index:index])
            start_index = index
            found_a = False
        index += 1
    return code_segments

memo = {}    
sum_complexities = 0
for code in codes:

    # get the first set of instructions using the numerical keypad
    first_level  = get_numerical_instructions(code)

    # take a small segment of a code and use recursion with memoization to find out how long it will be after 25 iterations
    def recurse(segment,count):
        if (segment,count) in memo.keys():
            return memo[(segment,count)]
        sequence = get_directional_instructions(segment)

        if count == 1:
            return len(sequence)
        
        else:
            codesum = 0
            segments = split_code_segments(sequence)
            for seg in segments:
                codesum += recurse(seg,count-1)
        
            memo[(segment,count)] = codesum
            return codesum  
    
    segments = split_code_segments(first_level)
    code_len = 0
    for s in segments:
        code_len += recurse(s,25)
    num_part = int("".join(code[:-1]))
    complexity = code_len * num_part
    print(complexity)
    sum_complexities += complexity
   
print(sum_complexities) 
