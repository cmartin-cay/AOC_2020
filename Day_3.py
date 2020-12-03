from itertools import repeat

from collections import namedtuple

with open("Day_3.txt") as f:
    forrest = f.readlines()

with open("Day_3_sample.txt") as f:
    sample_forrest = f.readlines()

forrest = [x.rstrip() for x in forrest]
sample_forrest = [x.rstrip() for x in sample_forrest]
width = len(forrest[0])
Point = namedtuple("Point", ['x', 'y'])
start_point = Point(x=0, y=0)
slope = (1, 3)
slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
tree_list = []
# slope = slopes[4]

"""
The forrest is 31 squares wide
The forrest is 323 squares tall
For Step 1, we travel over 3 and then down 1. So we need 323 steps
We can use some wraparound math in the x axis with modulus to
keep us in the initial dataset
"""

print(8 % 8)


def move(point: Point):
    x_pos = point.x + slope[0]
    y_pos = (point.y + slope[1]) % width
    point = Point(x=x_pos, y=y_pos)
    return point


for slope in slopes:
    trees_in_path = 0
    steps_taken = 0
    start_point = Point(x=0, y=0)
    while steps_taken < len(forrest) - 1:
        start_point = move(start_point)
        if forrest[start_point.x][start_point.y] == "#":
            trees_in_path += 1
        steps_taken += slope[0]
    tree_list.append(trees_in_path)

print(tree_list)
result = 1
for elem in tree_list:
    result *= elem
print(result)
