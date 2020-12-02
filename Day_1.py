import itertools
import time

with open("Day_1.txt") as f:
    expense_items = f.read().splitlines()

DESIRED_TOTAL = 2020
NUMBERS_TO_SUM = []
THREE_NUMBERS_TO_SUM = []
THREE_NUMBERS_TO_SUM_ALT = []
expense_items_list = sorted([int(x) for x in expense_items])
expense_items_set = set(expense_items_list)

"""
Part 1: Find 2 numbers in the expense items that sum to 2020
        Multiply them together
"""

part_1_start = time.time_ns()
for elem in expense_items_set:
    if (DESIRED_TOTAL - elem) in expense_items_set:
        NUMBERS_TO_SUM.extend([elem, DESIRED_TOTAL - elem])
        break

part_1 = (NUMBERS_TO_SUM[0] * NUMBERS_TO_SUM[1])
print(f"Part 1 answer is {part_1} and took {time.time_ns() - part_1_start}")

"""
Part 2: Find 3 numbers in the expense items that sum to 2020
        Multiply them together
"""


def find_three(values):
    for first in values:
        for second in values:
            first_plus_second = first + second
            if first_plus_second > DESIRED_TOTAL:
                continue
            elif (DESIRED_TOTAL - first_plus_second) in expense_items_set:
                THREE_NUMBERS_TO_SUM.extend([first, second, DESIRED_TOTAL - first_plus_second])
                return


part_2_start = time.time_ns()
find_three(expense_items_list)
print(THREE_NUMBERS_TO_SUM)
part_2 = THREE_NUMBERS_TO_SUM[0] * THREE_NUMBERS_TO_SUM[1] * THREE_NUMBERS_TO_SUM[2]
print(f"Part 2 answer is {part_2} and took {time.time_ns() - part_2_start}")

"""
Part 2 (alt):   Find 3 numbers in the expense items that sum to 2020
                Multiply them together
"""
combos = itertools.combinations(expense_items_list, 3)
part_2_alt_start = time.time_ns()


def find_three_alt(combos):
    for combo in combos:
        if sum(combo) == DESIRED_TOTAL:
            THREE_NUMBERS_TO_SUM_ALT.extend(list(combo))
            return


find_three_alt(combos)
print(THREE_NUMBERS_TO_SUM_ALT)
part_2_alt = THREE_NUMBERS_TO_SUM_ALT[0] * THREE_NUMBERS_TO_SUM_ALT[1] * THREE_NUMBERS_TO_SUM_ALT[2]
print(f"Part 2 alt answer is {part_2_alt} and took {time.time_ns() - part_2_alt_start}")
