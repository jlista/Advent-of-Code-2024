import math

with open("C:/Python/2024/day5input.txt", 'r') as file:

    # Parse input 

    lines = [line.strip() for line in file]
    split_ind = lines.index("")

    rules = []
    for rule in lines[0:split_ind]:
        spl = rule.split('|')
        rules.append((int(spl[0]), int(spl[1])))

    books = []
    for book in lines[split_ind+1:]:
        books.append([int(n) for n in book.split(',')])

    # Part 1

    sum = 0
    bad_orders = []
    good_orders = []
    for book in books:
        is_legal = True
        # Go through all rules, stopping if we find a rule that is broken
        for rule in rules:
            first = rule[0]
            last = rule[1]
            if first in book and last in book and book.index(first) > book.index(last):
                is_legal = False
                break
        # Sort the books into two lists, ones that break the rules and ones that do not
        if is_legal:
            good_orders.append(book)
        else:
            bad_orders.append(book)

    # sum up the middle elements of books that do not break the rules
    sumP1 = 0
    for book in good_orders:
        middle = int(book[math.floor(len(book)/2)])
        sumP1 += middle
    print(f"Part 1: {sumP1}")

    # PART 2

    sumP2 = 0
    for book in bad_orders:
        
        # cycle through the rules. Any time we find a pair of numbers in the wrong order, switch them and then
        # cycle through the rules again, repeating until they all pass
        is_legal = False
        ruleindex = -1
        while not is_legal:
            ruleindex += 1
            rule = rules[ruleindex]
            first = rule[0]
            last = rule[1]

            if first in book and last in book:
                firstindex = book.index(first)
                lastindex = book.index(last)
                if firstindex > lastindex:
                    # switch them
                    book[firstindex] = last
                    book[lastindex] = first
                    ruleindex = -1 # restart
            # if we reach the end of the rule list with none of them broken, the book has been fixed
            if ruleindex == len(rules) - 1:
                is_legal = True

        middle = int(book[math.floor(len(book)/2)])
        sumP2 += middle
    print(f"Part 2: {sumP2}")